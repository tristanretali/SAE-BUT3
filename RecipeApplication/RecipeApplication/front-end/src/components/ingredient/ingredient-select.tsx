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
];


export function IngredientSelect() {
  return (
    <Select
      items={ingredients}
      isMultiline={true}
      selectionMode="multiple"
      placeholder="Ingredients?"
      labelPlacement="outside"
      classNames={{
        base: "max-w-xs",
        trigger: "min-h-12 py-2",
      }}
      renderValue={(ingredients: SelectedItems<Ingredient>) => {
        return (
          <div className="flex flex-wrap gap-2">
            {ingredients.map((ingredient) => (
              <Badge key={ingredient.key}>{ingredient.textValue}</Badge>
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
