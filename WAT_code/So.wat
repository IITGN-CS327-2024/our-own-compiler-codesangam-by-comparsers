(module
	(func $store (param $value i32) (param $address i32)
        ;; Store the value at the specified address in memory
        (i32.store (local.get $address) (local.get $value))
    )

    (func $load (param $address i32) (result i32)
        (i32.load
        (local.get $address)  ;; Load value from specified address
        )
    )
	(func $sort (export "sort")
		(param $p0 i32)
		(param $p1 i32)
		(local $temp1 i32)
		(local $temp2 i32)
		(local $i i32)
		(local $j i32)
		local.set $temp1
		local.set $temp2
		loop
			local.get $i
			i32 const 0
			i32.add 
			local.set $i
			loop
				local.get $j
				i32 const 0
				i32.add 
				local.set $j
				local.get $j
				local.get $p1
				i32.lt_s
				br_if 0
			local.get $i
			local.get $p1
			i32.lt_s
			br_if 0
	)
)