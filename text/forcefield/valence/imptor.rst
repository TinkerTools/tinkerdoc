.. _label-imptor:

Improper Torsion
================

Commonly used in the AMBER force fields, it defines a hypothetical torsional angle for four atoms not successively bonded, e.g., a trigonal center. The functional form is similar to the proper torsion,

.. math::

   U = \sum_{n=1}^3 V_n[1+\cos(n\phi-\delta_n)],

where *n* is the periodicity and :math:`\delta_n` is the corresponding phase shift.
