from fastapi import FastAPI
from pydantic import BaseModel
import sys
import argparse

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
        print(final_rule)
        return {'final_rule': final_rule}
    except:
        raise Exception("Incorrect values entered.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--a',default='alert',type=str)
    parser.add_argument('--p',default='icmp',type=str)
    parser.add_argument('--sip',default='any',type=str)
    parser.add_argument('--sp',default='any',type=str)
    parser.add_argument('--dIp',default='$HOME_NET',type=str)
    parser.add_argument('--dP',default='any',type=str)
    parser.add_argument('--sId',type=str)
    parser.add_argument('--rId',default='1',type=str)

    args = parser.parse_args()

