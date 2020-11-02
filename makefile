run:
	python3
	python XORString.py $(ARGS)

if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)