import { useState } from "react";
import { Icons } from "../icons";
import { cn } from "@/lib/utils";
import { Button } from "../ui/button";

export function RecipeFavorite() {

	const [liked, setLiked] = useState(false)

	return (
		<Button onClick={() => setLiked(!liked)} className="absolute top-2 left-2" variant="link">
			<Icons.like className={cn("h-6 w-6 text-white",
				{ "fill-rose-500 text-rose-500": liked} )}/>
		</Button>
	)
}