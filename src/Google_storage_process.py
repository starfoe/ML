from sys import argv

import pandas as pd
from google.cloud import storage


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    return blobs


def main():
    blobs = list_blobs(bucket_name)
    name_list, cate_list = [], []
    full_bucket_name = 'gs://' + bucket_name + '/'
    # for blob in blobs:
    #     category = blob.name.split('/')[0]
    #     name_list.append(full_bucket_name + blob.name + ',' + category)
    for blob in blobs:
        filename_tmp = full_bucket_name + blob.name
        category = blob.name.split('/')[0]
        name_list.append(filename_tmp)
        cate_list.append(category)
    df = pd.DataFrame({'file_name': name_list, 'category': cate_list})
    df.to_csv(output_filename, header=False, index=False, sep=',')


if __name__ == '__main__':
    if len(argv) != 3:
        raise ValueError('Just two arguments are required')
    bucket_name = argv[1]
    output_filename = argv[2]
    main()
