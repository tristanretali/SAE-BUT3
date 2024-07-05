import { useState } from "react";
import { Icons } from "../icons";
import { cn, favoriteRecipe } from "@/lib/utils";
import { Button } from "../ui/button";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { Recipe } from "@/lib/recipe";
import { API_URL } from "@/lib/constants";

type RecipeFavoriteProps = {
	recipe: Recipe;
}

export function RecipeFavorite({recipe}: RecipeFavoriteProps) {

	const queryClient = useQueryClient()

	const { data: isLiked, isLoading } = useQuery({
		queryKey: ['favorites', recipe.id],
		queryFn: async () => {
			const response = await fetch(`${API_URL}/users/favorites`, {
				credentials: "include",
			})
			const data = await response.json()
			const recipes = data.recipes as Recipe[]
			return !!recipes.find(r => r.id === recipe.id)
		},
	})

	const mutation = useMutation({
		mutationFn: (recipeId: string) => {
			return favoriteRecipe(recipeId)
		},
		onSuccess: (data) => {
			queryClient.invalidateQueries({
				queryKey: ['favorites', recipe.id],
			})
 		},
	})

	return (
		<Button onClick={() => mutation.mutate(recipe.id)} className="absolute top-2 left-2" variant="link">
			<Icons.like className={cn("h-6 w-6 text-white",
				{ "fill-rose-500 text-rose-500": isLiked } )}/>
		</Button>
	)
}