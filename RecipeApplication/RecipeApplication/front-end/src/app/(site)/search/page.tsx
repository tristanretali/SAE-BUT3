"use client";

import { IngredientSelect } from "@/components/ingredient/ingredient-select";
import { RecipeCard } from "@/components/recipe/recipe-card";
import { Searchbar } from "@/components/searchbar";
import { API_URL } from "@/lib/constants";
import { Recipe } from "@/lib/recipe";
import { Spinner } from "@nextui-org/spinner";
import { useQuery } from "@tanstack/react-query";
import { useSearchParams } from "next/navigation";

const recipe = {
	name: "Pad thaï",
	recipeImage: "https://recipecontent.fooby.ch/17187_3-2_480-320.jpg",
	rating: 4.5,
	minutes: 30,
	diet: "vegan",
}

export default function Page() {

	const searchParams = useSearchParams()
	const search = searchParams.get('q') || ''

	const { data: recipes, isLoading } = useQuery<Recipe[]>({
		queryKey: ['recipes', search],
		queryFn: async () => {
			const response = await fetch(`${API_URL}/recipes/search?title=${search}`)
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
					<p>No recipes found for &quot;<span className="font-bold text-primary/50">{search}</span>&quot;</p>
				</div>
			)
		}
		return (
			<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-14 w-5/6">
				{recipes?.map((recipe) => (
					<RecipeCard key={recipe.instructions} recipe={recipe}/>
				))}
			</div>
		)
	}

	return (
		<div className="my-10 space-y-10 flex flex-col items-center w-screen">
			<Searchbar className="w-80" value={search}/>
			<div className="w-3/4">
				<IngredientSelect/>
			</div>
			{resultElement()}
		</div>
	)
}