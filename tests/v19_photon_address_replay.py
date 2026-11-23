"""Independent check of address-window arithmetic stated in PHOTON16 v0.13 record.
Not the original browser test or an optical hardware test.
"""
import collections,json
covered=[]
widths=collections.Counter()
for t in range(360):
    sector=t//120
    quad=(t%120)//30
    local=t%30
    low=(local*128)//30
    high=((local+1)*128)//30
    addresses=[quad*128+i for i in range(low,high)]
    # This source formula covers one quad's 128 positions per 30 ticks;
    # sector identity is separate in the spec, so include sector to preserve uniqueness.
    global_addresses=[sector*512+x for x in addresses]
    assert len(global_addresses)==len(set(global_addresses))
    covered.extend(global_addresses)
    widths[len(addresses)]+=1
result={
 'ticks':360,'distinct':len(set(covered)),'total_assignments':len(covered),
 'min_address':min(covered),'max_address':max(covered),
 'counts_per_tick':dict(sorted(widths.items())),
 'all_1536_covered':len(covered)==len(set(covered))==1536 and set(covered)==set(range(1536)),
 'status':'PASS' if len(covered)==len(set(covered))==1536 and widths=={4:264,5:96} else 'FAIL',
 'kind':'independent mathematical replay from authored formula, not original browser code'
}
print(json.dumps(result,indent=2))
with open('photon_arithmetic_results.json','w') as f:json.dump(result,f,indent=2)
assert result['status']=='PASS'
