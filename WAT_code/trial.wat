(module
	(func $add (export "add")
		(param $p0 i32)
		(param $p1 i32)
		(result i32)
		local.get $p0
		local.get $p1
		f32.add
		return
	)
	(func $sub (export "sub")
		(param $p0 i32)
		(param $p1 i32)
		(result i32)
		local.get $p0
		local.get $p1
		f32.sub
		return
	)
)