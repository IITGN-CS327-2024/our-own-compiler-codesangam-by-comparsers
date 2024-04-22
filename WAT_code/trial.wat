(module
	(func $store_value_at_address (param $value i32) (param $address i32)
        ;; Store the value at the specified address in memory
        (i32.store (local.get $address) (local.get $value))
    )

    (func $loadValueFromMemory (param $address i32) (result i32)
        (i32.load
        (local.get $address)  ;; Load value from specified address
        )
    )
	(func $add (export "add")
		(param $p0 i32)
		(param $p1 i32)
		(result i32)
		local.get $p0
		local.get $p1
		i32.add
		return
	)
	(func $sub (export "sub")
		(param $p0 i32)
		(param $p1 i32)
		(result i32)
		local.get $p0
		local.get $p1
		i32.sub
		return
	)
)