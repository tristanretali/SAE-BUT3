"use client";

import { Recipe, RecipeCard } from "@/components/recipe/recipe-card";
import { Searchbar } from "@/components/searchbar";
import { useSearchParams } from "next/navigation";

const recipe: Recipe = {
	name: "Pad thaï",
	recipeImage: "https://recipecontent.fooby.ch/17187_3-2_480-320.jpg",
	rating: 4.5,
	minutes: 30,
	diet: "vegan",
}

const recipe2: Recipe = {
	name: "Poulet curry",
	recipeImage: "https://static.750g.com/images/1200-630/91ab938d758f762c1f3f84286b121e53/adobestock-307737508.jpeg",
	rating: 4.2,
	minutes: 25,
	diet: "",
}

const recipes: Recipe[] = [
	recipe,
	recipe,
	recipe2,
	recipe,
	recipe2,
	recipe,
]

export default function Page() {

	const searchParams = useSearchParams()
	const search = searchParams.get('value') || ''

	const recipesResult = recipes.filter(recipe => recipe.name.toLowerCase().includes(search.toLowerCase()))

	return (
		<div className="my-10 space-y-10 flex flex-col items-center w-screen">
			<Searchbar className="w-80" value={search}/>
			<div className="grid grid-cols-3 gap-14 w-5/6">
				{recipesResult.map((recipe, index) => (
					<RecipeCard key={index} recipe={recipe}/>
				))}
			</div>
		</div>
	)
}