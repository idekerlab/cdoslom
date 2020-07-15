===================================================
Community Detection OSLOM
===================================================

This repository creates a CDAPS compatible community detection Docker image using OSLOM
packaged from http://www.oslom.org/

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

Dependencies
------------

* `Docker <https://www.docker.com/>`_
* `make <https://www.gnu.org/software/make/>`_ (to build)
* Python (to build)

Direct invocation
------------------

Version `0.3.0` can be directly pulled from `Dockerhub <https://hub.docker.com/>`_ with this command:

.. code-block::

   docker pull coleslawndex/cdoslom:0.3.0

Building
--------

.. code-block::

   git clone https://github.com/idekerlab/cdoslom
   cd cdoslom
   make dockerbuild

Run **make** command with no arguments to see other build/deploy options including creation of Docker image

.. code-block::

   make

Output:

.. code-block::

   clean                remove all build, test, coverage and Python artifacts
   clean-build          remove build artifacts
   clean-pyc            remove Python file artifacts
   clean-test           remove test and coverage artifacts
   lint                 check style with flake8
   test                 run tests quickly with the default Python
   test-all             run tests on every Python version with tox
   coverage             check code coverage quickly with the default Python
   docs                 generate Sphinx HTML documentation, including API docs
   servedocs            compile the docs watching for changes
   testrelease          package and upload a TEST release
   release              package and upload a release
   dist                 builds source and wheel package
   install              install the package to the active Python's site-packages
   dockerbuild          build docker image and store in local repository
   dockerpush           push image to dockerhub


Usage
-----

.. code-block::

   docker run -v coleslawndex/cdoslom:0.3.0 -h

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
