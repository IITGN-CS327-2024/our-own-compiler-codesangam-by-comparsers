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
	(func $caesarEncrypt (export "caesarEncrypt")
		(param $p0 i32)
		(param $p1 i32)
		(param $p2 i32)
		(local $i i32)
		(local $temp i32)
		i32.const 0
		local.set $i
		loop
			local.get $i
			i32.const 1
			i32.add
			local.set $i
			local.get $p0
			local.get $i
			i32.const 4
			i32.mul
			i32.add
			call $load
			local.set $temp
			local.get $temp
			local.get $p2
			i32.add
			i32.const 26
			i32.rem_u
			local.set $temp
			local.get $p0
			local.get $i
			i32.const 4
			i32.mul
			i32.add
			local.get $temp
			call $store
			local.get $i
			local.get $p1
			i32.lt_s
			br_if 0
	)
	(func $caesarDecrypt (export "caesarDecrypt")
		(param $p0 i32)
		(param $p1 i32)
		(param $p2 i32)
		(local $i i32)
		(local $temp i32)
		i32.const 0
		local.set $i
		loop
			local.get $i
			i32.const 1
			i32.add
			local.set $i
			local.get $p0
			local.get $i
			i32.const 4
			i32.mul
			i32.add
			call $load
			local.set $temp
			local.get $temp
			local.get $p2
			i32.sub
			local.set $temp
			(if $I0 (
			local.get $temp
			i32.const 0
			i32.lt_s
				) (then 
				local.get $temp
				i32.mul
				local.set $temp
			)
				(else
				)
			)
			local.get $temp
			i32.const 26
			i32.rem_u
			local.set $temp
			local.get $p0
			local.get $i
			i32.const 4
			i32.mul
			i32.add
			local.get $temp
			call $store
			local.get $i
			local.get $p1
			i32.lt_s
			br_if 0
	)
)