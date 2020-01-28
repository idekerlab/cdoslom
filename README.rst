===================================================
Community Detection Oslom
===================================================

.. image:: https://img.shields.io/pypi/v/cdoslom.svg
        :target: https://pypi.python.org/pypi/cdoslom

.. image:: https://img.shields.io/travis/idekerlab/cdoslom.svg
        :target: https://travis-ci.org/idekerlab/cdoslom

.. image:: https://readthedocs.org/projects/cdoslom/badge/?version=latest
        :target: https://cdoslom.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://requires.io/github/idekerlab/cdoslom/requirements.svg?branch=master
        :target: https://requires.io/github/idekerlab/cdoslom/requirements?branch=master
        :alt: Dependencies


Maps genes to terms

* Free software: BSD license
* Documentation: https://cdoslom.readthedocs.io.

Features
--------

- OSLOM (Order Statistics Local Optimization Method) is a dynamic method based on the local optimization of cluster statistical significance subject to random fluctuations.
- Work on any graph
- `param` input: edge list file in tab delimited format
- `param` directed: whether to treat edges as directed  *default: False*
- `param` singlet: True to leave singlet communities unmerged; False to merge communities of only one node with existing community of best modularity  *default: False*
- `param` seed: set random seed for the community detection process;must be nonnegative integer  *default: -1 (no seed)*
- `param` p_val: p value threshold to consider part of a graph as community; increase to get more communites/modules  *default: 0.1*
- `param` cp: coverage parameter to decide between taking some modules or their union; works like the reverse resolution parameter; bigger value leads to bigger communities  *default: 0.5*

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
