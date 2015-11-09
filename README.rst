=================
textblob-aptagger
=================

**As of TextBlob 0.11.0, TextBlob uses NLTK's averaged perceptron tagger by default. This package is no longer necessary.**

.. image:: https://badge.fury.io/py/textblob-aptagger.png
    :target: http://badge.fury.io/py/textblob-aptagger
    :alt: Latest version

.. image:: https://travis-ci.org/sloria/textblob-aptagger.png?branch=master
    :target: https://travis-ci.org/sloria/textblob-aptagger
    :alt: Travis-CI

A fast and accurate part-of-speech tagger based on the Averaged Perceptron. For use with `TextBlob`_.

Implementation by Matthew Honnibal, a.k.a. `syllog1sm <https://github.com/syllog1sm/>`_. Read more about it `here <http://honnibal.wordpress.com/2013/09/11/a-good-part-of-speechpos-tagger-in-about-200-lines-of-python/>`_.

Install
-------

If you have `pip <http://www.pip-installer.org/>`_ installed (you should), run ::

    $ pip install -U textblob-aptagger

Usage
-----
.. code-block:: python

    >>> from textblob import TextBlob
    >>> from textblob_aptagger import PerceptronTagger
    >>> blob = TextBlob("Simple is better than complex.", pos_tagger=PerceptronTagger())
    >>> blob.tags
    [('Simple', u'NN'), ('is', u'VBZ'), ('better', u'JJR'), ('than', u'IN'), ('complex', u'JJ')]

Requirements
------------

- Python >= 2.6 or >= 3.3

License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/sloria/textblob-aptagger/blob/master/LICENSE>`_ file for more details.

.. _TextBlob: https://textblob.readthedocs.org/
