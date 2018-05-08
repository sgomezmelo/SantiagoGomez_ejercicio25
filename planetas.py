import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-10
M = 1.989e+30

r_mercury = [2.133679072387218e-01,-3.727310311768299e-01,-5.058864779204983e-02]
v_mercury = [1.892057222101034e-02,1.513838055059527e-02,-4.995475648824679e-04]

r_tierra = [-6.857609665891080e-01,-7.327391341104329e-01,-6.644615610967885e-05 ]
v_tierra= [1.231562236067741e-02,-1.177303988314858e-02,1.210619824052227e-06]

r_jupiter = [-3.616450082845184,-4.014244339308792,9.754215806840760e-02]
v_jupiter = [5.517283470150529e-03,-4.691963322519999e-03,-1.039452586609281e-04]

r = np.array([r_mercury,r_tierra,r_jupiter])
v = np.array([v_mercury,v_tierra,v_jupiter])

R = np.zeros(3)
V = np.zeros(3)

for i in range(3):
    R[i]  = np.sqrt(np.sum(r[i,:]**2))
    V[i]  =  np.sqrt(np.sum(v[i,:])**2)

alfa = np.random.uniform(0.0,10.0,100)
b = V[0]**2/R[0]**(1-alfa)


plt.figure()
plt.hist(b)
plt.savefig('ProbabilidadBeta.png')
