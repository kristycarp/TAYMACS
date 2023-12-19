# TAYMACS
## _GROMACS (Taylor's Version)_
## Kristy Carpenter, 2023

A simple repo to add a little bit of TSwizzle to your molecular dynamics simulations. TAYMACS replaces the quotes that appear at the end of a successful GROMACS command with a random Taylor Swift lyric. All other GROMACS functionality remains unchanged.

### Setup
TAYMACS requires a couple of quick steps before you can run all the Swiftie MD simulations that your heart desires:
1. **Setup .bashrc**
TAYMACS requires a couple of small additions to your .bashrc file in order to run. You can automatically add these by running the `setup.sh` script:
```./setup.sh```

2. **Install requirements**
TAYMACS requires Python. And, in whatever environment you are using for your MD simulations, make sure that you have installed a version of **numpy** that is compatible with your Python version. If you are using conda to manage your environment, this installation is easy:
```conda install numpy```

### Usage
Usage is easy! Just use the `taymacs` command in place of the `gmx` command whenever you use GROMACS. For example, here is a quick way to make sure that TAYMACS is properly set up:
```taymacs pdb2gmx -h```

### Contact
Found a bug or typo? Please submit an Issue in this repo and I will do my best to follow up in a timely manner.
Want to chat about any other topic or concern, or interested in hiring a computational biologist with software engineering skills, experience with atomistic and coarse-grained molecular dynamics simulations, and too much Taylor Swift knowledge for her own good? Feel free to email me at kcarp@stanford.edu.
