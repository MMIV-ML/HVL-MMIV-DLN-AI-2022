HVL-MMIV-DLN-AI-2022 Setup for the Biomedical imaging course module


# Setting up your system for biomedical image processing and analysis


#### On Mac, Windows and Linux we will use the [command line](https://en.wikipedia.org/wiki/Command-line_interface#Command-line_interpreter) (shell)
See e.g. [Basic Unix Commands](https://people.duke.edu/~ccc14/pcfb/unix.html) and [Computing Skills for Biologists](https://computingskillsforbiologists.com) [[here](https://github.com/CSB-book/CSB)] if this is unfamiliar to you. See also the
[Unix Shell](http://swcarpentry.github.io/shell-novice) lessons (thanks to [Anne Fouilloux](https://www.mn.uio.no/geo/english/people/adm/annefou), UiO)

#### ... and luckily also the [Jupyter notebook](https://www.nature.com/articles/d41586-018-07196-1)
- for openness [!](https://www.nature.com/news/interactive-notebooks-sharing-the-code-1.16261) and reproduciblity [!](https://arxiv.org/pdf/1810.08055.pdf)


## Colab:
Alternatively, some of the Jupyter notebooks in the Labs can be executed on **Google Colaboratory**. Colaboratory, or “Colab” for short, is a product from Google Research. Colab allows anybody to write and execute arbitrary python code through the browser, and is especially well suited to machine learning, data analysis and education. More technically, Colab is a hosted Jupyter notebook service that requires no setup to use, while providing free access to computing resources including GPUs. Colab is free to use, and resources are not guaranteed and not unlimited, and the usage [resource limits](https://research.google.com/colaboratory/faq.html#resource-limits) sometimes fluctuate.

Colab code is executed in a virtual machine private to your account, i.e.

> you will need to [Create a Google Account](https://support.google.com/accounts/answer/27441?hl=en) if you not already have one (you don't need a Gmail account to create a Google Account as you can use your non-Gmail address).

Virtual machines are deleted when idle for a while, and have a maximum lifetime enforced by the Colab service.

Colab notebooks are stored in [Google Drive](https://drive.google.com/drive/my-drive), or can be loaded from [GitHub](https://github.com). Colab notebooks can be shared just as you would with Google Docs or Sheets. Simply click the Share button at the top right of any Colab notebook, or follow these Google Drive [file sharing instructions](https://support.google.com/drive/answer/2494822?co=GENIE.Platform%3DDesktop&hl=en).


## Anaconda:
We recommend installing Python via the [Anaconda Distribution](https://www.anaconda.com/download). Be sure to use the "Python 3.8" version. We will use the Conda Package Management System within the Anaconda Distribution. From the [documentation](https://conda.io/docs):
> Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer.

After the installation run `python --version` in a terminal window (in "**Anaconda Powershell Prompt**" if you are using Windows). If the output show "Python 3.8" (and "Anaconda") you are good to go.


## Atom:
Atom is a free and open-source text and source code editor for writing and editing text files e.g. YAML configuration files, Markdown files, JSON files, HTML files and others. By its developers it is called a "hackable text editor for the 21st Century" and is a useful tool in addition to the browser-based Jupyter notebook that we will use.
You can also **render markdown files** (e.g. local README.md files): Packages -> Markdow Preview -> Toggle Preview.<br>
Install Atom (Mac Windows Linux) from: https://flight-manual.atom.io/getting-started/sections/installing-atom

# ITK-SNAP:
ITK-SNAP is an open-source image analysis tool used to segment and label structures in 3D medical images. ITK-SNAP is supported on Mac, Windows and Linux and provides semi-automatic segmentation using active contour methods, as well as manual delineation and image navigation. You can read and interact with DICOM and NIFTI images, and plot time-course data. Download the newest release of ITK-SNAP at http://www.itksnap.org/pmwiki/pmwiki.php?n=Downloads.SNAP3


## Install and test the course environment

After you have successfully installed Anaconda, go through the following steps (if you are using Windows, be at the "Anaconda Prompt").

### Install Git:
```bash
conda install git
```
### Download the repository (you have likely done this already, and if so, you only need to do `git pull`):
```bash
git clone https://github.com/MMIV-ML/HVL-MMIV-DLN-AI-2022
cd HVL-MMIV-DLN-AI-2022/2-biomedical_imaging
```
### Configure the Python-environment for image processing and analysis:
```bash
conda env create -f environment-img.yml
```

### Activate the environment:
```bash
conda activate dln2022-img
```

### Install a Jupyter kernel:
```bash
python -m ipykernel install --user --name dln2022-img --display-name "DLN2022-IMG"
```

### Optionally - Jupyter Lab
You can (preferably) consider to use [JupyterLab](https://github.com/jupyterlab/jupyterlab), i.e. `> jupyter lab` <br>
(in addition to or insted of the `> jupyter notebook`)


### Test you installation:
Go through the notebook [`0-test-installation.ipynb`](https://nbviewer.jupyter.org/github/MMIV-ML/HVL-MMIV-DLN-AI-2022/blob/main/2-biomedical_imaging/0-test-installation.ipynb) in the `2-biomedical_imaging`-directory:
```bash
cd "2-biomedical_imaging"
jupyter notebook  (or, jupyter lab)
```

## Update:
The image processing and analysis code and environment will likely be updated during the course. Run the following commands regularly from your locally cloned repo in folder `HVL-MMIV-DLN-AI-2022`:
* Update code: `git pull`
* Update environment:
```bash
cd 2-biomedical_imaging
conda activate dln2022-img
conda env update -f environment-img.yml
```

# Unix Shell

Learners need to understand what files and directories are and what a working directory is. These concepts are covered in the
[Unix Shell](http://swcarpentry.github.io/shell-novice) lessons (thanks to [Anne Fouilloux](https://www.mn.uio.no/geo/english/people/adm/annefou), UiO)

# Programming with Python

The best way to learn how to program is to do something useful, so [this](http://swcarpentry.github.io/python-novice-inflammation) introduction to Python is built around a common scientific task: **data analysis** ("... _we are studying inflammation in patients who have been given a new treatment for arthritis, and need to analyze the first dozen data sets of their daily inflammation_ ..."); see also [here](https://github.com/swcarpentry/python-novice-inflammation).


## A note on R (tip for previous R users)

**It is possible to run R-scripts in Jupyter notebooks**  (Jupyter = Julia, Python and R).

If you want to continue working with R (*not part of this course*) you should:

- Be using the latest R version (https://www.r-project.org) and the RStudio Desktop [[download](https://rstudio.com/products/rstudio/download)] for your Windows, MacOS or Linux system.
- **Install the R kernel** by opening an R console and then follow the instructions at https://irkernel.github.io/installation
- Necessary (or new) R libraries should be installed via RStudio and the corresponding R environment.
- See also [here](https://datatofish.com/r-jupyter-notebook) and [here](https://developers.refinitiv.com/article/setup-jupyter-notebook-r).
- The [rpy2](https://github.com/rpy2/rpy2) interface to use R form Python is also possible (but can be a bit more messy).
