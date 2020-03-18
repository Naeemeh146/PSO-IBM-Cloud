from flask import Flask, render_template
from flask import request
import numpy as np
import functions
from restarts_PSO import ParticleSwarmOptimizer, Particle

app = Flask(__name__)

@app.route('/')
def hello_whale():
    # A = request.args.get('a')
    # B = request.args.get('b')
    # if A is not None and B is not None:
    #     C = np.mean([int(A), int(B)])
    #     return str(C)
    func = request.args.get('func')
    run  = request.args.get('run')
    if func is not None and run is not None:
        restarts_pso = ParticleSwarmOptimizer(int(func) , int(run))
        gbest = restarts_pso.optimize()
        return str(func) + ',' + str(run) + ',' + str(gbest[-1])
    return 'No Input'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')