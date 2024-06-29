import { Container, Flex, Box, Text, Button, useColorMode } from "@chakra-ui/react"
import { IoMoon } from "react-icons/io5"
import { LuSun } from "react-icons/lu"

const Navbar = () => {

   const { colorMode, toggleColorMode } = useColorMode()
   return (
      <Container maxW={"1200px"} my={4}>
         <Box
            py={4}
            my={4}
            borderRadius={5}
            bg={useColorMode().colorMode === "light" ? "gray.100" : "gray.700"}
         >
            <Flex justifyContent={"space-between"} alignItems={"center"} px={"20px"}>
               <Flex justifyContent={"center"} alignItems={"center"} gap={3} display={{ base: "none", sm: "flex" }}>
                  <img src="/react.png" alt="React Logo" width={50} height={50} />
                  <Text fontSize={"40px"}>+</Text>
                  <img src="/python.png" alt="Python Logo" width={50} height={50} />
                  <Text fontSize={"40px"}>=</Text>
                  <img src="/explode.png" alt="Explode Head" width={45} height={45} />
               </Flex>
               <Flex gap={3} alignItems={"center"}>
                  <Text fontSize={"lg"} fontWeight={500} display={{ base:"none", md:"block" }}>Faqihh</Text>
                  <Button onClick={toggleColorMode}>
                     {colorMode === "light" ? <IoMoon/>  : <LuSun size={20} />}
                  </Button>
               </Flex>
            </Flex>
         </Box>
      </Container>
   )
}

export default Navbar