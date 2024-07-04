"use client";

import { API_URL } from "@/lib/constants"
import { Spinner } from "@nextui-org/spinner";
import { useQuery } from "@tanstack/react-query"

export function RecipesCount() {

	const { data: recipesCount, isLoading, isError } = useQuery<number>({
		queryKey: ['recipesCount'],
		queryFn: async () => {
			const response = await fetch(`${API_URL}/recipes/count`)
			const data = await response.json()
			return data.count
		}
	})

	if (isError) {
		return <span className="text-red-500 font-bold mx-1">error</span>
	}

	if (isLoading) {
		return <Spinner size="sm" className="inline h-3 w-3 mx-1" classNames={{
				wrapper: "inline-block",
			}}/>
	}

	return (
		<span className="text-primary font-bold m-1">
			{recipesCount?.toLocaleString()}
		</span>
	)
}