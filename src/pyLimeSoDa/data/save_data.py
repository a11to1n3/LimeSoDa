import pandas as pd
import numpy as np
import pickle
import os
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri, vectors
from rpy2.robjects.conversion import localconverter

def r_to_pandas(r_obj):
    """Convert R object to pandas DataFrame with type checking"""
    if isinstance(r_obj, vectors.DataFrame):
        with localconverter(robjects.default_converter + pandas2ri.converter):
            return robjects.conversion.rpy2py(r_obj)
    elif isinstance(r_obj, (vectors.BoolVector, vectors.IntVector, vectors.FloatVector, vectors.StrVector)):
        # Convert vector to numpy array then to pandas Series/DataFrame
        arr = np.array(r_obj)
        if arr.ndim == 1:
            return pd.DataFrame(arr.reshape(-1, 1))
        return pd.DataFrame(arr)
    else:
        # Try general conversion
        try:
            with localconverter(robjects.default_converter + pandas2ri.converter):
                return robjects.conversion.rpy2py(r_obj)
        except Exception as e:
            print(f"Warning: Could not convert object of type {type(r_obj)}: {str(e)}")
            return None

def r_to_array(r_obj):
    """Convert R object to numpy array with type checking"""
    if isinstance(r_obj, (vectors.BoolVector, vectors.IntVector, vectors.FloatVector, vectors.StrVector)):
        return np.array(r_obj)
    else:
        try:
            return np.array(r_obj)
        except Exception as e:
            print(f"Warning: Could not convert object of type {type(r_obj)} to array: {str(e)}")
            return None

def load_rda_file(file_path):
    """Load RDA file using rpy2"""
    print(f"\nLoading RDA file: {file_path}")
    
    # Load the R data file
    robjects.r['load'](file_path)
    
    # Get list of objects in the R workspace
    obj_names = list(robjects.r('ls')())
    print(f"Objects found in RDA file: {obj_names}")
    
    if not obj_names:
        raise ValueError("No objects found in RDA file")
    
    # If there's only one object, use that
    main_obj_name = obj_names[0]
    print(f"\nUsing object: {main_obj_name}")
    
    # Get structure of the object
    print("\nObject structure:")
    print(robjects.r(f'str({main_obj_name})'))
    
    # Get the main object
    main_obj = robjects.globalenv[main_obj_name]
    
    # Try to get names of list components if it's a list
    try:
        component_names = list(main_obj.names)
        print(f"\nComponents found: {component_names}")
    except:
        component_names = []
        print("\nNo named components found")
    
    # Initialize return values
    dataset_df = None
    folds_array = None
    coordinates_df = None
    
    # Extract components
    try:
        for name in component_names:
            component = main_obj.rx2(name)
            print(f"\nProcessing component '{name}' of type {type(component)}")
            
            # Convert based on the component name and type
            if name == 'Dataset' or name.lower().endswith('dataset'):
                dataset_df = r_to_pandas(component)
                if dataset_df is not None:
                    print(f"Converted {name} to DataFrame with shape {dataset_df.shape}")
            
            elif name == 'Folds' or name.lower().endswith('folds'):
                folds_array = r_to_array(component)
                if folds_array is not None:
                    print(f"Converted {name} to array with shape {folds_array.shape}")
            
            elif name == 'Coordinates' or name.lower().endswith('coordinates'):
                coordinates_df = r_to_pandas(component)
                if coordinates_df is not None:
                    print(f"Converted {name} to DataFrame with shape {coordinates_df.shape}")
            
            else:
                print(f"Skipping unknown component: {name}")
    
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        raise
    
    # Print final conversion summary
    print("\nExtraction Summary:")
    print(f"Dataset: {dataset_df.shape if dataset_df is not None else 'Not found'}")
    print(f"Folds: {folds_array.shape if folds_array is not None else 'Not found'}")
    print(f"Coordinates: {coordinates_df.shape if coordinates_df is not None else 'Not found'}")
    
    return dataset_df, folds_array, coordinates_df

def save_data_npz(dataset_df, folds_array, coordinates_df, output_file='converted_data.npz'):
    """Save all data to a single compressed numpy file"""
    data_dict = {}
    
    # Save Dataset if available
    if dataset_df is not None:
        data_dict.update({
            'dataset_data': dataset_df.to_numpy(),
            'dataset_index': dataset_df.index.to_numpy(),
            'dataset_columns': np.array(dataset_df.columns)
        })
    
    # Save Folds if available
    if folds_array is not None:
        data_dict['folds'] = folds_array
    
    # Save Coordinates if available
    if coordinates_df is not None:
        data_dict.update({
            'coordinates_data': coordinates_df.to_numpy(),
            'coordinates_index': coordinates_df.index.to_numpy(),
            'coordinates_columns': np.array(coordinates_df.columns)
        })
    
    np.savez_compressed(output_file, **data_dict)
    print(f"Data saved to {output_file}")

def load_data_npz(file_path):
    """Load data from npz file"""
    loaded = np.load(file_path, allow_pickle=True)
    
    # Initialize return values
    dataset_df = None
    folds_array = None
    coordinates_df = None
    
    # Load Dataset if available
    if all(k in loaded for k in ['dataset_data', 'dataset_index', 'dataset_columns']):
        dataset_df = pd.DataFrame(
            loaded['dataset_data'],
            index=loaded['dataset_index'],
            columns=loaded['dataset_columns']
        )
    
    # Load Folds if available
    if 'folds' in loaded:
        folds_array = loaded['folds']
    
    # Load Coordinates if available
    if all(k in loaded for k in ['coordinates_data', 'coordinates_index', 'coordinates_columns']):
        coordinates_df = pd.DataFrame(
            loaded['coordinates_data'],
            index=loaded['coordinates_index'],
            columns=loaded['coordinates_columns']
        )
    
    return dataset_df, folds_array, coordinates_df

def convert_r_to_python(input_file, output_file=None, use_compression=True):
    """Convert R data to Python format and save to a single file"""
    print(f"\nConverting {input_file}...")
    
    # Load and parse the data
    dataset_df, folds_array, coordinates_df = load_rda_file(input_file)
    
    # Generate output filename if not provided
    if output_file is None:
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}_converted{'_npz' if use_compression else '_pkl'}"
        output_file = f"{output_file}.{'npz' if use_compression else 'pkl'}"
    
    # Save to file
    if use_compression:
        save_data_npz(dataset_df, folds_array, coordinates_df, output_file)
    else:
        with open(output_file, 'wb') as f:
            pickle.dump({
                'dataset': dataset_df,
                'folds': folds_array,
                'coordinates': coordinates_df
            }, f)
        print(f"Data saved to {output_file}")
    
    # Print summary
    print("\nConversion Summary:")
    if dataset_df is not None:
        print(f"Dataset shape: {dataset_df.shape}")
        print("\nDataset columns:", list(dataset_df.columns))
        print("\nFirst few rows of Dataset:")
        print(dataset_df.head())
    else:
        print("No Dataset found")
    
    if folds_array is not None:
        print(f"\nFolds array shape: {folds_array.shape}")
        print("First few elements of Folds:", folds_array[:5])
    else:
        print("\nNo Folds found")
    
    if coordinates_df is not None:
        print(f"\nCoordinates shape: {coordinates_df.shape}")
        print("\nCoordinates columns:", list(coordinates_df.columns))
        print("\nFirst few rows of Coordinates:")
        print(coordinates_df.head())
    else:
        print("\nNo Coordinates found")
    
    return dataset_df, folds_array, coordinates_df

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        use_compression = True if len(sys.argv) <= 3 else sys.argv[3].lower() == 'true'
        
        convert_r_to_python(input_file, output_file, use_compression)
    else:
        print("Usage: python script.py input_file [output_file] [use_compression]")
