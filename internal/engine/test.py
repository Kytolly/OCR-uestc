from output.output import *
from output.outputJson import *
from setting.message import *

records = [
    [ [(20, 30), (120, 30), (120, 90), (20, 90)],   'Python',        0.9],
    [ [(10, 10), (110, 10), (110, 90), (10, 90)],   'JavaScript',    0.8],
    [ [(5, 5), (105, 5), (105, 85), (5, 85)],       'C++',           0.7],
]

output = Output(1, statusOK=None, msgCode=None, records=None)
output.fit(records)
print(output._json()) 

oj = OutputJson(output, 'out', 'test2')  
oj.print()

data = output.serialize()
print(data.hex())

newout = Output.deserialize(data)
oj1 = OutputJson(newout, 'out', 'test2')  
oj1.print()