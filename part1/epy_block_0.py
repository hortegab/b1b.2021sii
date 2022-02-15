import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  
    

    def __init__(self,):  
        """Bloque Promediador """
        gr.sync_block.__init__(
            self,
            name='Time Average',   
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.acum_anterior=0
        self.Ntotales=0
        
    def work(self, input_items, output_items):
        x=input_items[0]
        N=len(x)
        self.Ntotales += N
        y=output_items[0]
        Acumulado=self.acum_anterior+np.cumsum(x)
        self.acum_anterior=Acumulado[-1]
        y[:]=Acumulado/self.Ntotales
        
        return len(x)
        

