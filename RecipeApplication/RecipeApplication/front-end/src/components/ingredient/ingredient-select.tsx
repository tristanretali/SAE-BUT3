import React from "react";
import {Select, SelectSection, SelectItem, SelectedItems} from "@nextui-org/select";
import { Badge } from "../ui/badge";

type Ingredient = {
  name: string;
  emoji: string;
};

const ingredients: Ingredient[] = [
  {name: "Tomato", emoji: "🍅"},
  {name: "Cheese", emoji: "🧀"},
  {name: "Bread", emoji: "🍞"},
  {name: "Lemon", emoji: "🍋"},
  {name: "Egg", emoji: "🥚"},
  {name: "Milk", emoji: "🥛"},
  {name: "Butter", emoji: "🧈"},
];


export function IngredientSelect() {
  return (
    <Select
      items={ingredients}
      isMultiline={true}
	  label="Ingredients"
      selectionMode="multiple"
      placeholder="Choose"
      labelPlacement="outside"
      classNames={{
		label: "w-32 flex items-center justify-center p-0",
        base: "max-w-60 h-10",
        trigger: "h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 shadow-none border-slate-500 border-[0.4px]",
      }}
      renderValue={(ingredients: SelectedItems<Ingredient>) => {
        return (
          <div className="flex gap-2 flex-nowrap">
            {ingredients.map((ingredient) => (
              <Badge variant="secondary" className="rounded-md px-1" key={ingredient.key}>{ingredient.data?.emoji}</Badge>
            ))}
          </div>
        );
      }}
    >
      {(ingredient) => (
        <SelectItem key={ingredient.name} textValue={ingredient.name}>
          <div className="flex gap-2 items-center">
            <p className="flex-shrink-0 text-lg">{ingredient.emoji}</p>
            <div className="flex flex-col">
              <span className="text-tiny text-default-400">{ingredient.name}</span>
            </div>
          </div>
        </SelectItem>
      )}
    </Select>
  );
}
