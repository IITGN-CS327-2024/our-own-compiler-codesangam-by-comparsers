(module
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
	(func $mul (export "mul")
		(param $p0 i32)
		(param $p1 i32)
		(result i32)
		local.get $p0
		local.get $p1
		i32.mul
		return
	)
	(func $div (export "div")
		(param $p0 i32)
		(param $p1 i32)
		(result i32)
		local.get $p0
		local.get $p1
		i32.div_u
		return
	)
	(func $mod (export "mod")
		(param $p0 i32)
		(param $p1 i32)
		(result i32)
		local.get $p0
		local.get $p1
		return
	)
)