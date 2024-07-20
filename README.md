# VLAI: Exploration and Exploitation based on Visual-Language Aligned Information for Robotic Object Goal Navigation

We proposed a new framework to explore and search for the target in unknown environment, Our work is based on [SemExp](https://github.com/devendrachaplot/Object-Goal-Navigation) implemented in PyTorch.

**Author:** Haonan Luo, Yijie Zeng, Li Yang, Kexun Chen, Zhixuan Shen, Fengmao lv

**Affiliation:** University of Groningen

## Visual-Language Aligned Information

Object Goal Navigation(ObjectNav) is the task that an agent need navigate to an instance of a specific category in an unseen en-
vironment through visual observations within limited time steps. This work can help people with disabilities expediently find and
obtain the items they need. To achieve efficient ObjectNav in unfamiliar environments, global perception capabilities, understand-
ing the regularities of space and semantics in the environment layout are significant. In this work, we propose an explicit-prediction
method called VLAI that utilizes visual-language alignment information to guide the agent’s exploration, unlike previous navi-
gation methods based on frontier potential prediction or egocentric map completion, which only leverage visual observations to
construct semantic maps, thus failing to help the agent develop a better global perception. Specifically, when predicting long-term
goals, we retrieve previously saved visual observations to obtain visual information around the frontiers based on their position on
the incrementally built incomplete semantic map. Then, we apply our designed Chat Describer to these visual information to obtain
detailed frontier object descriptions. The Chat Describer, a novel automatic-questioning approach deployed in Visual-to-Language,
is composed of Large Language Model(LLM) and the visual-to-language model(VLM), which has visual question-answering func-
tionality. In addition, we also obtain the semantic similarity of target object and frontier object categories. Ultimately, by combining
the semantic similarity and the boundary descriptions, the agent can predict the long-term goals more accurately. Our experiments
on the Gibson and HM3D datasets reveal that our VLAI approach yields significantly better results compared to earlier methods.

![image-20200706200822807](frame.pdf)

<!-- ## Requirements

- Ubuntu 20.04
- Python 3.8
- [habitat-lab](https://github.com/facebookresearch/habitat-lab) -->

## Installation

The code has been tested only with Python 3.7 on Ubuntu 20.04.

1. Installing Dependencies
- We use challenge-2022 versions of [habitat-sim](https://github.com/facebookresearch/habitat-sim) and [habitat-lab](https://github.com/facebookresearch/habitat-lab) as specified below:

- Installing habitat-sim:
```
git clone https://github.com/facebookresearch/habitat-sim.git
cd habitat-sim; git checkout tags/challenge-2022; 
pip install -r requirements.txt; 
python setup.py install --headless
python setup.py install # (for Mac OS)
```

- Installing habitat-lab:
```
git clone https://github.com/facebookresearch/habitat-lab.git
cd habitat-lab; git checkout tags/challenge-2022; 
pip install -e .
```

- Install [pytorch](https://pytorch.org/) according to your system configuration. The code is tested on pytorch v1.7.0 and cudatoolkit v11.4. If you are using conda:
```
conda install pytorch==1.7.0 torchvision==0.8.1 cudatoolkit=11.4 #(Linux with GPU)
conda install pytorch==1.7.0 torchvision==0.8.1 -c pytorch #(Mac OS)
```

- Install [detectron2](https://github.com/facebookresearch/detectron2/) according to your system configuration. 

2. Download HM3D datasets:

#### Habitat Matterport
Download [HM3D](https://aihabitat.org/datasets/hm3d/) dataset using download utility and [instructions](https://github.com/facebookresearch/habitat-sim/blob/089f6a41474f5470ca10222197c23693eef3a001/datasets/HM3D.md):
```
python -m habitat_sim.utils.datasets_download --username <api-token-id> --password <api-token-secret> --uids hm3d_minival
```

3. Download additional datasets

Download the [segmentation model](https://drive.google.com/file/d/1U0dS44DIPZ22nTjw0RfO431zV-lMPcvv/view?usp=share_link) in RedNet/model path.


## Setup
Clone the repository and install other requirements:
```
git clone https://github.com/31539lab/VLAI
cd VLAI/
pip install -r requirements.txt
```

### Setting up datasets
The code requires the datasets in a `data` folder in the following format (same as habitat-lab):
```
L3MVN/
  data/
    scene_datasets/
    matterport_category_mappings.tsv
    object_norm_inv_perplexity.npy
    versioned_data
    objectgoal_hm3d/
        train/
        val/
        val_mini/
```


### For evaluation: 
For evaluating the pre-trained model:
```
python main.py --split val --eval 1 --load pretrained/VLAI.pth
```
