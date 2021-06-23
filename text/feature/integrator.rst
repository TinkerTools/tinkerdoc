Integrators
===========

.. include:: ../replace.rst

.. table:: NVE methods.
   :widths: 50 50

   =============  =============
   Integrator     Availability
   =============  =============
   BEEMAN         8
   VERLET         8/9
   RESPA          8/9
   =============  =============

.. table:: NVT methods and availabilities.
   :widths: 50 50

   +-----------------+----------------------------------+
   | Integrator      | Thermostat                       |
   +=================+==================================+
   | - BEEMAN 8      | - ANDERSEN 8                     |
   | - VERLET 8/9    | - BERENDSEN 8                    |
   | - RESPA 8/9     | - BUSSI 8/9                      |
   |                 | - NOSE-HOOVER 8                  |
   +-----------------+----------------------------------+

.. table:: NPH methods and availabilities.
   :widths: 50 50

   +--------------+------------------+
   | Integrator   | Barostat         |
   +==============+==================+
   | - BEEMAN 8   | - BERENDSEN 8/9  |
   | - VERLET 8/9 | - MONTECARLO 8/9 |
   | - RESPA 8/9  |                  |
   +--------------+------------------+

.. table:: NPT methods and availabilities.
   :widths: 30 30 40

   +----------------------+-------------------+---------------------+
   | Integrator           | Thermostat        | Barostat            |
   +======================+===================+=====================+
   | - VERLET             | - ANDERSEN 8      | - BERENDSEN 8/9     |
   | - RESPA              | - BERENDSEN 8     | - MONTECARLO 8/9    |
   |                      | - BUSSI 8/9       |                     |
   |                      | - NOSE-HOOVER 8   |                     |
   +----------------------+-------------------+---------------------+
   | - VERLET             | (Built-in)        | LANGEVIN 9          |
   | - RESPA              |                   |                     |
   +----------------------+-------------------+---------------------+
   | BUSSI 8              | (Built-in)        | (Built-in)          |
   +----------------------+-------------------+---------------------+
   | NOSE-HOOVER 8/9      | (Built-in)        | (Built-in)          |
   +----------------------+-------------------+---------------------+

Integrators that need documentation are:

- BAOAB
- GHMC
- STOCHASTIC
- RIGIDBODY

.. toctree::

   integrator-verlet-respa
   integrator-nhc
   integrator-langevin-piston
