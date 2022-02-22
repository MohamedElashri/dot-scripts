"""
Use ROOT to make a TEfficiency plot on matplotlib
Usage: 

```
import ROOT
import matplotlib.pyplot as plt
eff = GetEfficiency(total,pass,nBins,binmin,binmax)
plt.errorbar(**eff,fmt="o:")
plt.ylabel("Efficiency")
plt.xlabel(var)
plt.show()	
```

"""
def GetEfficiency(total, pass, nBins, binmin, binmax):
    h_total = ROOT.TH1F("h_total","",nBins,binmin,binmax)
    h_pass  = ROOT.TH1F("h_pass","",nBins,binmin,bimax)
    h_total.SetDirectory(0)
    h_pass.SetDirectory(0)
    
    for x in total:
        h_total.Fill(x)
    for x in pass:
        h_pass.Fill(x)
        
    TE = ROOT.TEfficiency(h_pass,h_total)
    GR = TE.CreateGraph()
    i_x = ROOT.Double(0)
    i_y = ROOT.Double(0)
    nPoints = GR.GetN()
    
    Teff = np.zeros((nPoints,5))
    for i in range(nPoints):
        gr.GetPoint(i,i_x,i_y)
        i_ex = GR.GetErrorXlow(i)
        i_eyHi = GR.GetErrorYhigh(i)    
        i_eyLo = GR.GetErrorYlow(i)
        Teff[i] = np.array( [i_x,i_y,i_ex,i_eyLo,i_eyHi] )
        
    TE.IsA().Destructor(TE)
    h_total.IsA().Destructor(h_total)
    h_pass.IsA().Destructor(h_pass)
    
    eff = {
        'x'    : Teff[:,0],
        'y'    : Teff[:,1],
        #'xerr' : Teff[:,2], ## IF NEEDED
        'yerr' : [ Teff[:,3], Teff[:,4] ]
    }
    return eff
