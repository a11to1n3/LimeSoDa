from LimeSoDa import list_datasets, load_dataset
import pandas as pd
import json

def get_dataset_stats():
    """Generate statistics for all LimeSoDa datasets."""
    all_stats = {}
    dataset_list = list_datasets()
    feature_stats = {}
    
    for dataset_id in dataset_list:
        try:
            data = load_dataset(dataset_id)
            
            if dataset_id == "Overview_Datasets":
                continue
                
            dataset = data['Dataset']
            coords = data['Coordinates']
            
            stats = {
                'n_samples': len(dataset),
                'n_features': len(dataset.columns),
                'has_coordinates': not isinstance(coords, float)
            }
            
            feature_dist = {}
            for col in dataset.columns:
                feature_dist[col] = {
                    'mean': dataset[col].mean(),
                    'std': dataset[col].std(), 
                    'min': dataset[col].min(),
                    'max': dataset[col].max(),
                    'median': dataset[col].median(),
                    '25th': dataset[col].quantile(0.25),
                    '75th': dataset[col].quantile(0.75)
                }
            
            all_stats[dataset_id] = stats
            feature_stats[dataset_id] = feature_dist
            
        except Exception as e:
            print(f"Error loading dataset {dataset_id}: {str(e)}")
            
    with open('feature_distributions.json', 'w') as f:
        json.dump(feature_stats, f, indent=2)
    
    stats_df = pd.DataFrame.from_dict(all_stats, orient='index')
    
    return stats_df

def main():
    stats = get_dataset_stats()
    
    print("\nDataset Statistics Summary:")
    print("==========================")
    print(f"Total number of datasets: {len(stats)}")
    print("\nDetailed Statistics:")
    print(stats)
    
    stats.to_csv('dataset_statistics.csv')
    print("\nStatistics saved to dataset_statistics.csv")

if __name__ == "__main__":
    main()