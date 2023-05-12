from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RuleInputs(BaseModel):
    action : str
    protocol : str
    source_ip : str
    source_port : str
    dest_ip  : str
    dest_port : str
    sid  : str
    rev_num  : str
    msg : str

#Snort Rule Generator
@app.post('/rule/')
async def make_rule(inputs: RuleInputs):
    try:
        final_rule =""
        final_rule += inputs.action
        final_rule += " " + inputs.protocol
        final_rule += " " + inputs.source_ip
        final_rule += " " + inputs.source_port
        final_rule += " -> " + inputs.dest_ip
        final_rule += " " + inputs.dest_port
        final_rule += " ( msg:\"" + inputs.msg
        final_rule += "\"; sid:" + inputs.sid
        final_rule += "; rev:" + inputs.rev_num + "; )"
        return {'final_rule': final_rule}
    except:
        raise Exception("Incorrect values entered.")
