(module
	(memory (export "memory") 1)
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
		i32.const 0
		local.set $temp1
		i32.const 0
		local.set $temp2
		local.get $p1
		i32.const 1
		i32.add
		local.set $p1
		i32.const 0
		local.set $i
		loop
			local.get $i
			i32.const 1
			i32.add
			local.set $i
			i32.const 0
			local.set $j
			loop
				local.get $j
				i32.const 1
				i32.add
				local.set $j
				local.get $p0
				i32.const 4
				local.get $j
				i32.mul
				i32.add
				i32.const 4
				i32.sub
				call $load
				local.set $temp1
				local.get $p0
				i32.const 4
				local.get $j
				i32.mul
				i32.add
				call $load
				local.set $temp2
				local.get $temp1
				local.get $temp2
				i32.gt_s
				(if 
					(then 
					local.get $temp1
					local.get $p0
					i32.const 4
					local.get $j
					i32.mul
					i32.add
					call $store
					local.get $temp2
					local.get $p0
					i32.const 4
					local.get $j
					i32.mul
					i32.add
					i32.const 4
					i32.sub
					call $store
				)
					(else
					)
				)
				local.get $j
				local.get $p1
				local.get $i
				i32.sub
				i32.const 1
				i32.sub
				i32.lt_s
				br_if 0
				end
			local.get $i
			local.get $p1
			i32.lt_s
			br_if 0
			end
	)
)