from __future__ import absolute_import
import argparse
from model.pytorch.dcrnn_supervisor import DCRNNSupervisor
from lib.utils import load_graph_data
from yaml.loader import Loader
import yaml
from __future__ import print_function
from __future__ import division
import json


def train():
    """Train the DCRNN model based on the data from our config files"""


def main(args):
    with open(args.config_filename) as f:
        supervisor_config = yaml.load(f, Loader=Loader)

        graph_pkl_filename = supervisor_config['data'].get(
            'graph_pkl_filename')
        sensor_ids, sensor_id_to_ind, adj_mx = load_graph_data(
            graph_pkl_filename)
        for i in range(10):
            supervisor = DCRNNSupervisor(
                random_seed=i, adj_mx=adj_mx, **supervisor_config)
            supervisor.train()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_filename', default=None, type=str,
                        help='Configuration filename for restoring the model.')
    parser.add_argument('--use_cpu_only', default=False,
                        type=bool, help='Set to true to only use cpu.')
    args = parser.parse_args()
    main(args)


def predict():
    """Run predictions on our test set based on the model we trained"""

# Get commandline arguments to inform what function we want to use
parser = argparse.ArgumentParser()
parser.add_argument("context", help="specify what pipeline to run")
args = parser.parse_args()

# If the argument "train" is specified, run our training function
if args.context == "train":
    train()
# If the argument "test" is specified, run our test function
elif args.context == "predict":
    predict()

#TODO: Add test context
