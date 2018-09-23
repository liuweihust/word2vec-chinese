from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from datasets import news

datasets_map = {
    'news': news,
}


def get_dataset(name, dataset_dir="./"):
    """Given a dataset name and a split_name returns a Dataset.

    Args:
        name: String, the name of the dataset.
        split_name: A train/test split name.
        dataset_dir: The directory where the dataset files are stored.
        file_pattern: The file pattern to use for matching the dataset source files.
        reader: The subclass of tf.ReaderBase. If left as `None`, then the default
            reader defined by each dataset is used.
    Returns:
        A `Dataset` class.
    Raises:
        ValueError: If the dataset `name` is unknown.
    """
    if name not in datasets_map:
        raise ValueError('Name of dataset unknown %s' % name)
    return datasets_map[name]
