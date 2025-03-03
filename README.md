# Project Setup

This guide will help you set up and run the project on your local machine.

## **1. Set up the Virtual Environment**

First, create a virtual environment for the project. This isolates the dependencies required for the project from your system's Python installation.

```bash
python -m venv .venv
```

## **2. Activate the Virtual Environment**

Once the virtual environment is created, activate it:

**For Windows**
```bash
.venv\Scripts\activate
```

**For Linux/macOS**
```bash
source .venv/bin/activate
```
 
## **3. Install the Dependencies**
```bash
pip install -r requirements.txt
```

## **4. Compile the Project (if necessary)**
If you make any changes to the project or need to compile the project into an executable, use the compile.ps1 script. This script will bundle your Python project into an executable.

Run the following command in PowerShell to compile:
```bash
.\compile.ps1
```

Once compiled, the executable will be available in the dist folder.