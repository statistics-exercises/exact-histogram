try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

x = [0,1,3,4,5,6,0,1,2,3,4,5,6]
var = np.ones(14)*1/6
var[0] = 0
for i in range(7) : var[7+i] = scipy.stats.norm.pmf(i,6,0.5)
line1=line( x, var )

axislabels=["x", "P(x)"]

class UnitTests(unittest.TestCase) :
    def test_plot(self) :
        assert(check_plot([],exppatch=line1,explabels=axislabels,explegend=False,output=True))
