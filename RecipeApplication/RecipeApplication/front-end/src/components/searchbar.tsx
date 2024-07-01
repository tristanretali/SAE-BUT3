"use client";

import { Optional } from "@tanstack/react-query";
import { Button } from "./ui/button";
import { Input } from "./ui/input";
import { cn } from "@/lib/utils";

type SearchbarProps = {
	className: string;
}

export function Searchbar({ className }: Optional<SearchbarProps, "className">) {
	return (
		<div className={cn("inline-flex space-x-2", className)}>
			<Input className="border-slate-500 border-[0.4px] w-3/4" placeholder="Banana toast?">
			</Input>
			<Button className="w-1/4">
				search!
			</Button>
		</div>
	)
}