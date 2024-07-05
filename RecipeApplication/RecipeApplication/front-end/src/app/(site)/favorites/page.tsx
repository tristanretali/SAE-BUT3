"use client";

import { RecipeCard } from "@/components/recipe/recipe-card";
import { API_URL } from "@/lib/constants";
import { Recipe } from "@/lib/recipe";
import { Spinner } from "@nextui-org/spinner";
import { useQuery } from "@tanstack/react-query";

export default function Page() {

	const { data: recipes, isLoading } = useQuery<Recipe[]>({
		queryKey: ['favorites'],
		queryFn: async () => {
			const response = await fetch(`${API_URL}/users/favorites`, {
				credentials: "include",
			})
			const data = await response.json()
			return data.recipes
		}
	})

	const resultElement = () => {
		if (isLoading) {
			return (
				<div className="flex flex-col items-center justify-center h-full space-y-3">
					<Spinner size="md" className="inline h-10 w-10"/>
					Loading recipes...
				</div>
			)
		}
		if (recipes?.length === 0) {
			return (
				<div className="flex flex-col items-center justify-center h-full space-y-3">
					<h1 className="font-bold text-3xl font-heading text-primary">Oh no!</h1>
					<p>No recipes</p>
				</div>
			)
		}
		return (
			<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-14 w-5/6">
				{recipes?.map((recipe, index) => (
					<RecipeCard key={index} recipe={recipe}/>
				))}
			</div>
		)
	}

	return (
		<div className="my-10 space-y-10 flex flex-col items-center w-screen">
			{resultElement()}
		</div>
	)
}