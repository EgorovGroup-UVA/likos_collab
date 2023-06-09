Initial conditions for test.png

# 3D LAMMPS simulation for binary mixtures of ultrasoft repulsive particles
# Initialization
units lj
dimension 3
atom_style atomic
pair_style gem 2.5
boundary p p p

variable n1 equal 4950
variable n2 equal 550

# System definition
region box block 0 10 0 10 0 10
create_box 2 box
create_atoms 1 random ${n1} 123456 box
create_atoms 2 random ${n2} 234567 box

# Simulation settings
mass 1 1 
mass 2 1
pair_coeff 1 1 1.0 1.0 2
pair_coeff 2 2 1.0 1.0 4
pair_coeff 1 2 1.0 1.07 3

# Energy minimization
thermo 10
minimize 1.0e-4 1.0e-6 1000 10000

# Equilibration
fix nve all nve
fix langevin all langevin 1.0 1.0 0.1 345678
timestep 0.005
run 5000


# Visualization
unfix nve 
unfix langevin
thermo 50
variable kinetic_energy equal ke
variable potential_energy equal pe
variable pressure equal press
fix ave_time all ave/time 10 1 10 v_kinetic_energy v_potential_energy file energy3.dat
dump dump all atom 50 output2.lammpstrj

# Run
fix nve all nve
fix langevin all langevin 1.0 1.0 0.01 345678
timestep 0.0005
compute myRDF all rdf 100 1 1 cutoff 2.0
fix myfix all ave/time 100 1 10000 c_myRDF[1] c_myRDF[2] c_myRDF[3] file oneone_thr.txt mode vector
#first column is center bin, 2nd is g(r), 3rd is r
run 10000

