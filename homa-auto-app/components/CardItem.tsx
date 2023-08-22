import { Button, Center } from "native-base";
import React from "react";

interface CardItemProps {
  children: React.ReactNode;
}
export const CardItem = ({ children }: CardItemProps) => {
  return (
    <Center
      flex={1}
      borderRadius={"md"}
      bg={"gray.200"}
      borderColor={"amber.300"}
      h={40}
      w={"100%"}
      m={1}
      rounded={"md"}
      shadow={2}
    >
      {children}
      <Button colorScheme={"purple"} variant={"outline"}>
        Edit device
      </Button>
    </Center>
  );
};
