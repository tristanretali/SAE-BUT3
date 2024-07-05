import { useState } from "react";
import { Icons } from "../icons";
import { cn, favoriteRecipe } from "@/lib/utils";
import { Button } from "../ui/button";
import { useMutation } from "@tanstack/react-query";
import { Recipe } from "@/lib/recipe";

type RecipeFavoriteProps = {
	recipe: Recipe;
}

export function RecipeFavorite({recipe}: RecipeFavoriteProps) {

	const [liked, setLiked] = useState(false)

	const mutation = useMutation({
		mutationFn: () => favoriteRecipe(recipe.id),
		onSuccess: (data) => {
			setLiked(data.liked)
 		},
	})

	return (
		<Button onClick={() => mutation.mutate} className="absolute top-2 left-2" variant="link">
			<Icons.like className={cn("h-6 w-6 text-white",
				{ "fill-rose-500 text-rose-500": liked} )}/>
		</Button>
	)
}