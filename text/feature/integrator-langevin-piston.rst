Langevin Piston Integrator (NPT)
================================

.. include:: ../replace.rst

|doc9|

There are two implementations of the Langevin Piston integrator in Tinker9.

Implementation 1
----------------

This implementation is contributed from Wei Yang's group at Florida State University. This is a leap-frog style single time-step isotropic integrator similar to the one in CHARMM. The keywords used to invoke this method are:

.. code-block:: text

   integrator lpiston
   friction        20

or

.. code-block:: text

   thermostat lpiston
   barostat   lpiston
   friction        20

It was suggested to set the keyword :ref:`FRICTION <KEY-FRICTION>` to 20 for this integrator.

Implementation 2
----------------

This implements the Langevin Piston integrator in two ways: a single time-step integrator similar to Velocity-Verlet and a multiple time-step integrator similar to RESPA. They can be employed by the following keywords, respectively. The thermostat method is built in the integrator, thus the thermostat keyword is ignored.

.. code-block:: text

   # Velocity-Verlet Style
   barostat     langevin
   integrator     verlet

   # RESPA Style
   barostat     langevin
   integrator      respa

.. seealso::

   - New usage
      - :ref:`BAROSTAT <KEY-BAROSTAT>` [LANGEVIN]
         Must be set to LANGEVIN.
      - :ref:`FRICTION <KEY-FRICTION>` [real]
         Sets the value of the frictional coefficient in 1/ps for the Langevin dynamics of piston. The default is 20 in the absence of the keyword.
      - :ref:`VOLUME-TRIAL <KEY-VOLUME-TRIAL>` [integer]
         This keyword is borrowed from the Monte Carlo barostat to set the number of molecular dynamics steps between two changes in the periodic box size. The default is 1 step in the absence of the keyword.
      - :ref:`PRINTOUT <KEY-PRINTOUT>` [integer]
         Sets the number of box size changes between writes of the instantaneous pressure. The default value 0 will not print the instantaneous pressure. **This feature is in development.**
   - Relavent keywords
      - :ref:`ANISO-PRESSURE <KEY-ANISO-PRESSURE>`
         Invokes anisotropic cell fluctuations. **This feature is being tested.**
      - `SEMIISO-PRESSURE`
         Invokes isotropic cell fluctuations in the xy-plane and independent fluctuation in the z-axis. **This feature is in development, and this new keyword will be documented.**
      - :ref:`INTEGRATOR <KEY-INTEGRATOR>` [VERLET / RESPA]
         Only VERLET and RESPA are valid values.
      - :ref:`RESPA-INNER <KEY-RESPA-INNER>` [real]
         The program listens to the RESPA-INNER keyword to set the length of inner time-step in femtosecond only if the RESPA version is used.
      - :ref:`TAU-PRESSURE <KEY-TAU-PRESSURE>` [real]
         Tinker9 does not change its default value.
      - :ref:`TAU-TEMPERATURE <KEY-TAU-TEMPERATURE>` [real]
         Tinker9 does not change its default value.
   - Ignored keywords
      - :ref:`THERMOSTAT <KEY-THERMOSTAT>`
         The integrator uses a built-in thermostat.
      - :ref:`VOLUME-SCALE <KEY-VOLUME-SCALE>`
         The integrator uses molecular scaling if holonomic constraints are used, or atomic scaling otherwise.
