"use client";

import { Optional } from "@tanstack/react-query";
import { Button } from "./ui/button";
import { Input } from "./ui/input";
import { cn } from "@/lib/utils";
import { useState } from "react";
import Link from "next/link";

type SearchbarProps = {
	value: string;
	className: string;
}

export function Searchbar({ className, value }: Partial<SearchbarProps>) {

	const [searchValue, setSearchValue] = useState(value);

	return (
		<div className={cn("inline-flex space-x-2", className)}>
			<Input className="border-slate-500 border-[0.4px] w-3/4" placeholder="Banana toast?" onChange={(e) => setSearchValue(e.target.value)} value={searchValue}>
			</Input>
			<Button className="w-1/4" asChild>
				<Link href={`/search?value=${searchValue}`}>search!</Link>
			</Button>
		</div>
	)
}