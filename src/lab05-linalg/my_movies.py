import pandas as pd
import numpy as np
np.random.seed(42)
    
def generate_movie_data(n=5):
    '''
    generate movie data for n movies
    '''
    data = {
        'Action': np.random.randint(-2, 3, size=n),
        'Comedy': np.random.randint(-2, 3, size=n),
        'Romance': np.random.randint(-2, 3, size=n)
    }
    movie_data = pd.DataFrame(data, index=[f"movie{i}" for i in range(n)])
    return movie_data


def generate_data(row_name="user", n=5, features=['action','comedy','romance']):
    '''
    this does the same as the last function, but it is more general / flexible
    '''

    data = {}
    for f in features:
        data[f] = np.random.randint(-2, 3, size=n)

    df = pd.DataFrame(data)
    df.index = [f"{row_name}{i}" for i in range(n)]
    return df

if __name__ == "__main__":

    movie_features_df = generate_movie_data()
    movie_features_df.to_csv('data/movie_data.csv')

    # Generate synthetic data
    user_pref_df = generate_data()
    user_pref_df.to_csv('data/user_data.csv')


    
    