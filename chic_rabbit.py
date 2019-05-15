def solve(heads,legs):
    error_msg="No solution"
    rabbit_count=0 
    chicken_count=0 
    for chicken_count in range(0,heads+1):
        rabbit_count=heads-chicken_count
        totallegs=4*rabbit_count+2*chicken_count
        if(totallegs==legs):
            print(chicken_count,rabbit_count)
        else:
            print(error_msg)
