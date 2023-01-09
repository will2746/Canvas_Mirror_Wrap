{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP2t+sABnctzGsMTiL4OaFb",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/will2746/Canvas_Mirror_Wrap/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "S4xEFYaPkG-v"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# An AI Research Paper Summarizer"
      ],
      "metadata": {
        "id": "h863mBj_kJv_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "! pip install --upgrade openai\n",
        "! pip install PyMuPDF\n",
        "! pip install transformers\n",
        "!pip install streamlit\n",
        "!pip install pyngrok\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KePvCn6NkQnV",
        "outputId": "9abe42ad-8309-43cc-e57e-31845df82a5f"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: openai in /usr/local/lib/python3.8/dist-packages (0.26.0)\n",
            "Requirement already satisfied: requests>=2.20 in /usr/local/lib/python3.8/dist-packages (from openai) (2.25.1)\n",
            "Requirement already satisfied: aiohttp in /usr/local/lib/python3.8/dist-packages (from openai) (3.8.3)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.8/dist-packages (from openai) (4.64.1)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.8/dist-packages (from requests>=2.20->openai) (2.10)\n",
            "Requirement already satisfied: chardet<5,>=3.0.2 in /usr/local/lib/python3.8/dist-packages (from requests>=2.20->openai) (4.0.0)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.8/dist-packages (from requests>=2.20->openai) (1.24.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.8/dist-packages (from requests>=2.20->openai) (2022.12.7)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.8/dist-packages (from aiohttp->openai) (1.3.1)\n",
            "Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /usr/local/lib/python3.8/dist-packages (from aiohttp->openai) (4.0.2)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.8/dist-packages (from aiohttp->openai) (1.3.3)\n",
            "Requirement already satisfied: charset-normalizer<3.0,>=2.0 in /usr/local/lib/python3.8/dist-packages (from aiohttp->openai) (2.1.1)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.8/dist-packages (from aiohttp->openai) (22.2.0)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.8/dist-packages (from aiohttp->openai) (1.8.2)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.8/dist-packages (from aiohttp->openai) (6.0.3)\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: PyMuPDF in /usr/local/lib/python3.8/dist-packages (1.21.1)\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: transformers in /usr/local/lib/python3.8/dist-packages (4.25.1)\n",
            "Requirement already satisfied: tokenizers!=0.11.3,<0.14,>=0.11.1 in /usr/local/lib/python3.8/dist-packages (from transformers) (0.13.2)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.8/dist-packages (from transformers) (3.8.2)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.8/dist-packages (from transformers) (6.0)\n",
            "Requirement already satisfied: huggingface-hub<1.0,>=0.10.0 in /usr/local/lib/python3.8/dist-packages (from transformers) (0.11.1)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.8/dist-packages (from transformers) (2.25.1)\n",
            "Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.8/dist-packages (from transformers) (2022.6.2)\n",
            "Requirement already satisfied: numpy>=1.17 in /usr/local/lib/python3.8/dist-packages (from transformers) (1.21.6)\n",
            "Requirement already satisfied: tqdm>=4.27 in /usr/local/lib/python3.8/dist-packages (from transformers) (4.64.1)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.8/dist-packages (from transformers) (21.3)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.8/dist-packages (from huggingface-hub<1.0,>=0.10.0->transformers) (4.4.0)\n",
            "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.8/dist-packages (from packaging>=20.0->transformers) (3.0.9)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.8/dist-packages (from requests->transformers) (1.24.3)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.8/dist-packages (from requests->transformers) (2.10)\n",
            "Requirement already satisfied: chardet<5,>=3.0.2 in /usr/local/lib/python3.8/dist-packages (from requests->transformers) (4.0.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.8/dist-packages (from requests->transformers) (2022.12.7)\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.8/dist-packages (1.16.0)\n",
            "Requirement already satisfied: pympler>=0.9 in /usr/local/lib/python3.8/dist-packages (from streamlit) (1.0.1)\n",
            "Requirement already satisfied: tzlocal>=1.1 in /usr/local/lib/python3.8/dist-packages (from streamlit) (1.5.1)\n",
            "Requirement already satisfied: blinker>=1.0.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (1.5)\n",
            "Requirement already satisfied: packaging>=14.1 in /usr/local/lib/python3.8/dist-packages (from streamlit) (21.3)\n",
            "Requirement already satisfied: altair>=3.2.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (4.2.0)\n",
            "Requirement already satisfied: pyarrow>=4.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: tornado>=5.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (6.0.4)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (13.0.1)\n",
            "Requirement already satisfied: importlib-metadata>=1.4 in /usr/local/lib/python3.8/dist-packages (from streamlit) (5.2.0)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.8/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.8/dist-packages (from streamlit) (2.8.2)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: typing-extensions>=3.10.0.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (4.4.0)\n",
            "Requirement already satisfied: protobuf<4,>=3.12 in /usr/local/lib/python3.8/dist-packages (from streamlit) (3.19.6)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.8/dist-packages (from streamlit) (1.21.6)\n",
            "Requirement already satisfied: pandas>=0.21.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (1.3.5)\n",
            "Requirement already satisfied: pydeck>=0.1.dev5 in /usr/local/lib/python3.8/dist-packages (from streamlit) (0.8.0)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: requests>=2.4 in /usr/local/lib/python3.8/dist-packages (from streamlit) (2.25.1)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (5.2.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19 in /usr/local/lib/python3.8/dist-packages (from streamlit) (3.1.30)\n",
            "Requirement already satisfied: semver in /usr/local/lib/python3.8/dist-packages (from streamlit) (2.13.0)\n",
            "Requirement already satisfied: watchdog in /usr/local/lib/python3.8/dist-packages (from streamlit) (2.2.1)\n",
            "Requirement already satisfied: validators>=0.2 in /usr/local/lib/python3.8/dist-packages (from streamlit) (0.20.0)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.8/dist-packages (from altair>=3.2.0->streamlit) (4.3.3)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.8/dist-packages (from altair>=3.2.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.8/dist-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.8/dist-packages (from altair>=3.2.0->streamlit) (0.12.0)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.8/dist-packages (from gitpython!=3.1.19->streamlit) (4.0.10)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.8/dist-packages (from importlib-metadata>=1.4->streamlit) (3.11.0)\n",
            "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.8/dist-packages (from packaging>=14.1->streamlit) (3.0.9)\n",
            "Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.8/dist-packages (from pandas>=0.21.0->streamlit) (2022.7)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.8/dist-packages (from python-dateutil->streamlit) (1.15.0)\n",
            "Requirement already satisfied: chardet<5,>=3.0.2 in /usr/local/lib/python3.8/dist-packages (from requests>=2.4->streamlit) (4.0.0)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.8/dist-packages (from requests>=2.4->streamlit) (2.10)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.8/dist-packages (from requests>=2.4->streamlit) (2022.12.7)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.8/dist-packages (from requests>=2.4->streamlit) (1.24.3)\n",
            "Requirement already satisfied: commonmark<0.10.0,>=0.9.0 in /usr/local/lib/python3.8/dist-packages (from rich>=10.11.0->streamlit) (0.9.1)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.6.0 in /usr/local/lib/python3.8/dist-packages (from rich>=10.11.0->streamlit) (2.6.1)\n",
            "Requirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.8/dist-packages (from validators>=0.2->streamlit) (4.4.2)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.8/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit) (5.0.0)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.8/dist-packages (from jinja2->altair>=3.2.0->streamlit) (2.0.1)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.8/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (22.2.0)\n",
            "Requirement already satisfied: importlib-resources>=1.4.0 in /usr/local/lib/python3.8/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (5.10.1)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.8/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.19.2)\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pyngrok\n",
            "  Downloading pyngrok-5.2.1.tar.gz (761 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m761.3/761.3 KB\u001b[0m \u001b[31m15.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: PyYAML in /usr/local/lib/python3.8/dist-packages (from pyngrok) (6.0)\n",
            "Building wheels for collected packages: pyngrok\n",
            "  Building wheel for pyngrok (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pyngrok: filename=pyngrok-5.2.1-py3-none-any.whl size=19792 sha256=2555da46e491277155b368206e0b82e510fbea59a47b02c9e51139e0201722ca\n",
            "  Stored in directory: /root/.cache/pip/wheels/5d/f2/70/526da675d32f17577ec47ac4c663084efe39d47c826b6c3bb1\n",
            "Successfully built pyngrok\n",
            "Installing collected packages: pyngrok\n",
            "Successfully installed pyngrok-5.2.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Part 1. importing stuff"
      ],
      "metadata": {
        "id": "nWnNdMSIkSqk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Step 1: Importing a document:\n",
        "\n",
        "# Import the fitz module from PyMuPDF\n",
        "import os\n",
        "import fitz \n",
        "import math\n",
        "import openai\n",
        "import re\n",
        "import os\n",
        "import transformers\n",
        "import streamlit as st\n",
        "from transformers import GPT2TokenizerFast\n"
      ],
      "metadata": {
        "id": "M7rmgcmEkhA4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 502
        },
        "outputId": "35a16d9e-6521-47ab-f873-44eccbcd70d4"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ImportError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-13-21b6272ad64e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mos\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mtransformers\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 11\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     12\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtransformers\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mGPT2TokenizerFast\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/streamlit/__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     53\u001b[0m \u001b[0m__version__\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_STREAMLIT_VERSION_STRING\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 55\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdelta_generator\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mDeltaGenerator\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0m_DeltaGenerator\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     56\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mproto\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mRootContainer_pb2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mRootContainer\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0m_RootContainer\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m from streamlit.runtime.caching import (\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/streamlit/delta_generator.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     36\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtyping_extensions\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mFinal\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mLiteral\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     37\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 38\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mconfig\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcursor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0menv_util\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlogger\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mruntime\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtype_util\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mutil\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     39\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcursor\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mCursor\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     40\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0melements\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0malert\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mAlertMixin\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/streamlit/cursor.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     16\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mutil\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 18\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mruntime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscriptrunner\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mget_script_run_ctx\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     19\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     20\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/streamlit/runtime/__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     14\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     15\u001b[0m \u001b[0;31m# Explicitly re-export public symbols from runtime.py\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 16\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mruntime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mruntime\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mRuntime\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mRuntime\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     17\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mruntime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mruntime\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mRuntimeConfig\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mRuntimeConfig\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mruntime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mruntime\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mRuntimeState\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mRuntimeState\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/streamlit/runtime/runtime.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mconfig\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlogger\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mget_logger\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 26\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mproto\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mBackMsg_pb2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mBackMsg\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     27\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mproto\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mForwardMsg_pb2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mForwardMsg\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     28\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mruntime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mapp_session\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mAppSession\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/streamlit/proto/BackMsg_pb2.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;31m# source: streamlit/proto/BackMsg.proto\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\"\"\"Generated protocol buffer code.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mgoogle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprotobuf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minternal\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mbuilder\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0m_builder\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mgoogle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprotobuf\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mdescriptor\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0m_descriptor\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mgoogle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprotobuf\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mdescriptor_pool\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0m_descriptor_pool\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mImportError\u001b[0m: cannot import name 'builder' from 'google.protobuf.internal' (/usr/local/lib/python3.8/dist-packages/google/protobuf/internal/__init__.py)",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Setting the file location"
      ],
      "metadata": {
        "id": "20p5LAlrkast"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Setting the Pdf Document folder\n",
        "pdf_path_in ='/content/cleantechnol-04-00029.pdf'"
      ],
      "metadata": {
        "id": "jXOGE2enk3Fd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Streamlit Stuff"
      ],
      "metadata": {
        "id": "5OmbQ-cSjwwm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "st.write(\"\"\"\n",
        "  # Talk To Papers\n",
        "  This app will help you better understand any research paper faster\"\"\")\n",
        "\n",
        "# Create a file uploader widget\n",
        "uploaded_file = st.file_uploader(\"Choose a PDF to upload:\", type=\"pdf\")\n",
        "\n",
        "# Create a text input widget\n",
        "text_input = st.text_input(\"Enter your question:\")\n",
        "\n",
        "# Create a chatbot function\n",
        "def chatbot_response(input_text):\n",
        "  # You can add your own chatbot logic here\n",
        "  return \"I'm sorry, I can't understand what you're trying to ask.\"\n",
        "\n",
        "# Display the uploaded PDF and chatbot response\n",
        "if uploaded_file is not None:\n",
        "  st.write(f\"PDF Loaded: {uploaded_file.name}\")\n",
        "\n",
        "  summary = create_summaries(uploaded_file)\n",
        "\n",
        "  st.write('### Summary')\n",
        "  st.write(f'{summary}')\n",
        "\n",
        "  chatbot_response = chatbot_response(text_input)\n",
        "\n",
        "\n",
        "  st.write(f\"Chatbot: {chatbot_response}\")\n",
        "\n"
      ],
      "metadata": {
        "id": "MyT8HvJcj2uI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## All the Functions"
      ],
      "metadata": {
        "id": "uinIvCgxk72J"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "#Creating code that will extract the PDF\n",
        "\n",
        "def extract_text_from_pdf(pdf_path):\n",
        "    # Open the PDF file\n",
        "    pdf_document = fitz.open(pdf_path)\n",
        "\n",
        "    # Iterate through each page of the PDF\n",
        "    text1=''\n",
        "    for page in pdf_document:\n",
        "        # Extract the text from the page\n",
        "        text = page.get_text(\"text\")\n",
        "        text1= text1 + text\n",
        "\n",
        "    return text1\n",
        "\n",
        "#this gets rid of any refrences at the end\n",
        "def delete_after_references(text):\n",
        "    # Split the text into a list of lines\n",
        "    lines = text.split(\"\\n\")\n",
        "\n",
        "    # Find the index of the line containing \"References\"\n",
        "    for i, line in enumerate(lines):\n",
        "        if \"References\" in line:\n",
        "            index = i\n",
        "            break\n",
        "\n",
        "    # Delete all lines after the line containing \"References\"\n",
        "    lines = lines[:index+1]\n",
        "\n",
        "    # Join the lines back into a single string\n",
        "    text = \"\\n\".join(lines)\n",
        "    return text\n",
        "\n",
        "# Finding headings in a text file:\n",
        "\n",
        "def find_headings(document_text):\n",
        "    # Open the text file and read its contents into a string\n",
        "    lines = []\n",
        "    headers = '1'\n",
        "    beans = 0\n",
        "\n",
        "    while headers:\n",
        "        beans = beans+1\n",
        "    # Use the regular expression to find all lines that start with \"1.\"\n",
        "        headers = re.findall(r'^{}\\.\\s+(.*)'.format(beans), document_text, re.M)\n",
        "\n",
        "        headers = ' '.join(headers)\n",
        "        # need to account for roman numerals as well here... for another day...\n",
        "\n",
        "        header1= str(beans) + \". \" + headers\n",
        "        lines.append(header1)\n",
        "\n",
        "    # Print the lines\n",
        "    lines.pop()\n",
        "    lines.insert(0, 'Abstract')\n",
        "\n",
        "    return lines\n",
        "\n",
        "\n",
        "# this function takes a text file and a list of headers, it looks through the\n",
        "# paper for the headings, then it takes the headers and it finds the text in those sections\n",
        "# It stores them in a list for later\n",
        "def get_text_between(file_contents,paper_headings):\n",
        "    # Check if the file exists\n",
        "    output={}\n",
        "    for i in range(len(paper_headings)):\n",
        "\n",
        "        if i < len(paper_headings)-1:\n",
        "            # Find the starting index of the text\n",
        "            start_index = file_contents.find(paper_headings[i])\n",
        "\n",
        "            # Find the ending index of the text\n",
        "            end_index = file_contents.find(paper_headings[i+1])\n",
        "        else:\n",
        "            # Find the starting index of the text\n",
        "            start_index = file_contents.find(paper_headings[i])\n",
        "\n",
        "            # Find the ending index of the text\n",
        "            end_index = len(file_contents)\n",
        "\n",
        "        # Extract the text between the starting and ending indices\n",
        "        text = file_contents[start_index:end_index]\n",
        "        output[paper_headings[i]] = text\n",
        "\n",
        "    return output\n",
        "\n",
        "def split_dictionary_values(d):\n",
        "  # Import the BertTokenizer class\n",
        "  from transformers import BertTokenizer\n",
        "\n",
        "  # Initialize the BertTokenizer\n",
        "  tokenizer = GPT2TokenizerFast.from_pretrained(\"gpt2\")\n",
        "\n",
        "  # Create a new dictionary to store the updated key-value pairs\n",
        "  d_new = {}\n",
        "\n",
        "  # Iterate over the key-value pairs in the dictionary\n",
        "  for key, value in d.items():\n",
        "    # Tokenize the value\n",
        "    tokens = tokenizer.tokenize(value)\n",
        "\n",
        "    # If the value is over 4000 tokens, split it in half and add the two halves to the new dictionary\n",
        "    if len(tokens) > 3000:\n",
        "      half = len(tokens) // 2\n",
        "      # Encode the value as a string to get the token IDs\n",
        "      token_ids = tokenizer.encode(value)\n",
        "      # Split the token IDs in half and decode them\n",
        "      value1 = tokenizer.decode(token_ids[:half])\n",
        "      value2 = tokenizer.decode(token_ids[half:])\n",
        "      # Add the two halves to the new dictionary\n",
        "      d_new[key + \" part 1\"] = value1\n",
        "      d_new[key + \" part 2\"] = value2\n",
        "    else:\n",
        "      # If the value is not over 4000 tokens, just add it to the new dictionary\n",
        "      d_new[key] = value\n",
        "\n",
        "  # Replace the original dictionary with the new one\n",
        "  d = d_new\n",
        "  return d\n",
        "      # Recursively call the function on the modified dictionary\n",
        "\n",
        "# Test the function\n",
        "\n",
        "# Running GPT-3\n",
        "def create_summaries(input_text_path):\n",
        "\n",
        "    # Set the API key\n",
        "    final_text=''\n",
        "    openai.api_key = \"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\"\n",
        "    for key, value in input_text_path.items():\n",
        "\n",
        "        # Set the prompt\n",
        "        prompt = (\n",
        "            f\"Section Title: {key}\\n\\n\"\n",
        "            f\"{value}\\n\\n\"\n",
        "            \"please summarize this excerpt from a scientific research paper in as much detail as possible, if applicable, include any key findings and suggestions for future research\\n\"\n",
        "        )\n",
        "\n",
        "        # Set the number of completions\n",
        "        num_completions = 1\n",
        "\n",
        "        # Generate completions\n",
        "        completions = openai.Completion.create(\n",
        "            engine='text-davinci-003',\n",
        "            prompt=prompt,\n",
        "            max_tokens=1500,\n",
        "            temperature=.7,\n",
        "            top_p=.8)\n",
        "        final_text=final_text+completions.choices[0].text\n",
        "\n",
        "        # Return the first completion\n",
        "    return final_text\n",
        "\n",
        "\n",
        "    #Summarize the whole paper:\n",
        "def summarize_paper(input_text):\n",
        "\n",
        "    # Set the API key\n",
        "    openai.api_key = \"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\"\n",
        "\n",
        "    # Set the prompt\n",
        "    prompt = ('provide a summary of these summaries from a paper include key findings and suggestions for future reserach'+input_text\n",
        "\n",
        "    )\n",
        "\n",
        "    # Set the number of completions\n",
        "    num_completions = 1\n",
        "\n",
        "    # Generate completions\n",
        "    completions = openai.Completion.create(\n",
        "        engine='text-davinci-003',\n",
        "        prompt=prompt,\n",
        "        max_tokens=1000,\n",
        "        temperature=.7,\n",
        "        top_p=.8)\n",
        "\n",
        "      # Return the first completion\n",
        "    print(completions.choices[0].text)\n",
        "    return completions.choices[0].text\n",
        "\n",
        "\n",
        "    # Print the completion\n",
        "\n",
        "def big_daddy(pdf_file_location):\n",
        "\n",
        "  # Running the first function to extract text from the PDF\n",
        "  text_file=extract_text_from_pdf(pdf_path_in)\n",
        "\n",
        "  #this file gets rid of all the text after the refrences (v important!)\n",
        "  document_text=delete_after_references(text_file)\n",
        "\n",
        "  # finding the headings of the paper (kinda genious)\n",
        "  paper_headings = find_headings(document_text)\n",
        "\n",
        "  # This function breaks the text into sections by Abstract, intro and so on\n",
        "  broked_text= get_text_between(document_text, paper_headings)\n",
        "\n",
        "  machine= split_dictionary_values(broked_text)\n",
        "\n",
        "  # This calles OpenAi to summarize the text\n",
        "  paper_summaries=create_summaries(machine)\n",
        "\n",
        "  #this one summarizes the summaries\n",
        "  summarize_paper(paper_summaries)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hPjW1jblkYt_",
        "outputId": "a5d72b38-63f9-4d38-b60b-885f02175c4a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Token indices sequence length is longer than the specified maximum sequence length for this model (1604 > 1024). Running this sequence through the model will result in indexing errors\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## The Big Daddy Function that runs everything!"
      ],
      "metadata": {
        "id": "BrXJ4Ch4lHxI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "big_daddy(pdf_path_in)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 713
        },
        "id": "H1_RsebElHS9",
        "outputId": "df791b0d-263b-4cc8-f25a-c8680a75c767"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Abstract', '1. Introduction', '2. Energy Storage Resources', '3. Energy Storage Technologies', '4. Energy Storage Modeling', '5. Discussions', '6. Conclusions', '7. Challenges and Future Works']\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "OSError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mHTTPError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/huggingface_hub/utils/_errors.py\u001b[0m in \u001b[0;36mhf_raise_for_status\u001b[0;34m(response, endpoint_name)\u001b[0m\n\u001b[1;32m    238\u001b[0m     \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 239\u001b[0;31m         \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mraise_for_status\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    240\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0mHTTPError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/requests/models.py\u001b[0m in \u001b[0;36mraise_for_status\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    942\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mhttp_error_msg\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 943\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mHTTPError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhttp_error_msg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    944\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mHTTPError\u001b[0m: 401 Client Error: Unauthorized for url: https://huggingface.co/gpt3/resolve/main/tokenizer_config.json",
            "\nThe above exception was the direct cause of the following exception:\n",
            "\u001b[0;31mRepositoryNotFoundError\u001b[0m                   Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/transformers/utils/hub.py\u001b[0m in \u001b[0;36mcached_file\u001b[0;34m(path_or_repo_id, filename, cache_dir, force_download, resume_download, proxies, use_auth_token, revision, local_files_only, subfolder, user_agent, _raise_exceptions_for_missing_entries, _raise_exceptions_for_connection_errors, _commit_hash)\u001b[0m\n\u001b[1;32m    408\u001b[0m         \u001b[0;31m# Load from URL or cache if already cached\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 409\u001b[0;31m         resolved_file = hf_hub_download(\n\u001b[0m\u001b[1;32m    410\u001b[0m             \u001b[0mpath_or_repo_id\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/huggingface_hub/utils/_validators.py\u001b[0m in \u001b[0;36m_inner_fn\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    123\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 124\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mfn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    125\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/huggingface_hub/file_download.py\u001b[0m in \u001b[0;36mhf_hub_download\u001b[0;34m(repo_id, filename, subfolder, repo_type, revision, library_name, library_version, cache_dir, user_agent, force_download, force_filename, proxies, etag_timeout, resume_download, token, local_files_only, legacy_cache_layout)\u001b[0m\n\u001b[1;32m   1066\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1067\u001b[0;31m                 metadata = get_hf_file_metadata(\n\u001b[0m\u001b[1;32m   1068\u001b[0m                     \u001b[0murl\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/huggingface_hub/utils/_validators.py\u001b[0m in \u001b[0;36m_inner_fn\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    123\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 124\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mfn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    125\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/huggingface_hub/file_download.py\u001b[0m in \u001b[0;36mget_hf_file_metadata\u001b[0;34m(url, token, proxies, timeout)\u001b[0m\n\u001b[1;32m   1375\u001b[0m     )\n\u001b[0;32m-> 1376\u001b[0;31m     \u001b[0mhf_raise_for_status\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mr\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1377\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/huggingface_hub/utils/_errors.py\u001b[0m in \u001b[0;36mhf_raise_for_status\u001b[0;34m(response, endpoint_name)\u001b[0m\n\u001b[1;32m    267\u001b[0m             )\n\u001b[0;32m--> 268\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mRepositoryNotFoundError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    269\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mRepositoryNotFoundError\u001b[0m: 401 Client Error. (Request ID: Root=1-63b65431-56d6ea85626cf7c167d300ed)\n\nRepository Not Found for url: https://huggingface.co/gpt3/resolve/main/tokenizer_config.json.\nPlease make sure you specified the correct `repo_id` and `repo_type`.\nIf the repo is private, make sure you are authenticated.\nInvalid username or password.",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mOSError\u001b[0m                                   Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-64-44d177dafa85>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mbig_daddy\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpdf_path_in\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-63-d8c1feb47ab2>\u001b[0m in \u001b[0;36mbig_daddy\u001b[0;34m(pdf_file_location)\u001b[0m\n\u001b[1;32m    167\u001b[0m   \u001b[0mbroked_text\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0mget_text_between\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdocument_text\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpaper_headings\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    168\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 169\u001b[0;31m   \u001b[0mmachine\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0msplit_text\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbroked_text\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    170\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    171\u001b[0m   \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmachine\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-63-d8c1feb47ab2>\u001b[0m in \u001b[0;36msplit_text\u001b[0;34m(inputs)\u001b[0m\n\u001b[1;32m     90\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     91\u001b[0m   \u001b[0;31m# Initialize the GPT2TokenizerFast\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 92\u001b[0;31m   \u001b[0mtokenizer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mGPT2TokenizerFast\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfrom_pretrained\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'gpt3'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     93\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     94\u001b[0m   \u001b[0;31m# Initialize a list to store the split text\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/transformers/tokenization_utils_base.py\u001b[0m in \u001b[0;36mfrom_pretrained\u001b[0;34m(cls, pretrained_model_name_or_path, *init_inputs, **kwargs)\u001b[0m\n\u001b[1;32m   1722\u001b[0m                 \u001b[0;31m# Try to get the tokenizer config to see if there are versioned tokenizer files.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1723\u001b[0m                 \u001b[0mfast_tokenizer_file\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFULL_TOKENIZER_FILE\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1724\u001b[0;31m                 resolved_config_file = cached_file(\n\u001b[0m\u001b[1;32m   1725\u001b[0m                     \u001b[0mpretrained_model_name_or_path\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1726\u001b[0m                     \u001b[0mTOKENIZER_CONFIG_FILE\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/transformers/utils/hub.py\u001b[0m in \u001b[0;36mcached_file\u001b[0;34m(path_or_repo_id, filename, cache_dir, force_download, resume_download, proxies, use_auth_token, revision, local_files_only, subfolder, user_agent, _raise_exceptions_for_missing_entries, _raise_exceptions_for_connection_errors, _commit_hash)\u001b[0m\n\u001b[1;32m    422\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    423\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0mRepositoryNotFoundError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 424\u001b[0;31m         raise EnvironmentError(\n\u001b[0m\u001b[1;32m    425\u001b[0m             \u001b[0;34mf\"{path_or_repo_id} is not a local folder and is not a valid model identifier \"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    426\u001b[0m             \u001b[0;34m\"listed on 'https://huggingface.co/models'\\nIf this is a private repository, make sure to \"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mOSError\u001b[0m: gpt3 is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo with `use_auth_token` or log in with `huggingface-cli login` and pass `use_auth_token=True`."
          ]
        }
      ]
    }
  ]
}