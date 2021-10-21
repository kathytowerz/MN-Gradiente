# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:51:32 2021

@author: Kathleen Lucía Torres Mancilla 298944
         Francisco Javier Vite Mimila 299043
         
Linear Solve: Gradiente descendente

Dejar en una función el método del gradiente.

"""
import numpy as np
'''
El objetivo es resolver Ax = b
Entonces para ello, hicimos lo siguiente:

Ax - b --> Discrepancia de un tanto para un x tanteado

Por facilidad, definimos el error cuadrado total como

(Ax - b)^2 

Que matricialmente se puede expresar como:

(Ax - b)' (Ax - b) = Error total cuadrado

Derivamos y encontramos que:

dE = 2A'Ax - 2A'b 

La idea es minimizar el error total cuadrado, porque
al hacerlo, llegaríamos al único mínimo del paraboloide
que es cuando (Ax - b)^2 = 0 y entonces, esto implicaría
que Ax = b y por ende x sería la solución del sistema de 
ecuaciones.
'''

#A = [[1,2,3],[1,2,3],[1,2,4]]

#mi_producto(A, transpuesta(A))
#x_nuevo = x_viejo - k * Gradiente
 
#Sistema de ecuaciones que se va a resolver:
A_coef = np.array([[2.0, 1.0, -3.0], [5.0, -4.0, 1.0], [1.0, -1.0, -4.0]])
b_coef = np.array([7.0, -19.0, 4.0])

x_sol = np.array([1.0, 1.0, 1.0])


def gradient(x, A, b):
	element_1 = np.dot(np.transpose(A),np.dot(A, x))
	element_2 = np.dot(np.transpose(A), b)
	return element_1 - element_2

def linear_solve(M, v, x_start, umbral, max_iter):
    for i in range(max_iter):
        print(x_start)
        x_start = x_start - umbral * gradient(x_start, M, v)
    return x_start

print(linear_solve(A_coef, b_coef, x_sol, 0.002, 1000))
'''
#def linear_solve(A, b, x_start, umbral = 0.001, max_iter = 1000)
###

#Tasa de aprendizaje.
k = 0.002 #Parámetros de ajuste o hiperparámetros
for i in range(1000):
	print(x_sol)
	x_sol = x_sol  - k * gradient(x_sol, A_coef, b_coef)

print(np.dot(A_coef,x_sol))
'''
