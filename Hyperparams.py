{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Hyperparams.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/hannape/CNN-pierwsze-podejscie/blob/master/Hyperparams.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "metadata": {
        "id": "A8nFF7T0g1OH",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "class Hyperparams:\n",
        "    '''Hyper parameters'''\n",
        "    \n",
        "    # pipeline\n",
        "    prepro = False  # if True, run `python prepro.py` first before running `python train.py`.\n",
        "\n",
        "    vocab = \"PE abcdefghijklmnopqrstuvwxyz'.?\" # P: Padding E: End of Sentence\n",
        "\n",
        "    # data\n",
        "    data = \"/data/private/voice/LJSpeech-1.0\"\n",
        "    # data = \"/data/private/voice/nick\"\n",
        "    test_data = 'harvard_sentences.txt'\n",
        "    max_duration = 10.0\n",
        "\n",
        "    # signal processing\n",
        "    sr = 22050 # Sample rate.\n",
        "    n_fft = 2048 # fft points (samples)\n",
        "    frame_shift = 0.0125 # seconds\n",
        "    frame_length = 0.05 # seconds\n",
        "    hop_length = int(sr*frame_shift) # samples.\n",
        "    win_length = int(sr*frame_length) # samples.\n",
        "    n_mels = 80 # Number of Mel banks to generate\n",
        "    power = 1.2 # Exponent for amplifying the predicted magnitude\n",
        "    n_iter = 50 # Number of inversion iterations\n",
        "    preemphasis = .97 # or None\n",
        "    max_db = 100\n",
        "    ref_db = 20\n",
        "\n",
        "    # model\n",
        "    embed_size = 256 # alias = E\n",
        "    encoder_num_banks = 16\n",
        "    decoder_num_banks = 8\n",
        "    num_highwaynet_blocks = 4\n",
        "    r = 5 # Reduction factor. Paper => 2, 3, 5\n",
        "    dropout_rate = .5\n",
        "\n",
        "    # training scheme\n",
        "    lr = 0.001 # Initial learning rate.\n",
        "    logdir = \"logdir/01\"\n",
        "    sampledir = 'samples'\n",
        "    batch_size = 32\n"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}