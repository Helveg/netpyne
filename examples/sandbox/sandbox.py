
from neuron import h
h.load_file('stdrun.hoc')

pc = h.ParallelContext()
pc.set_maxstep(10)

h.dt = 0.1
tstop = 1.0
s = h.Section()
t = h.Vector()
v = h.Vector()
v.record(s(0.5)._v_)
#t.record(h._ref_t)

h.stdinit()
pc.psolve(tstop)

print list(v)