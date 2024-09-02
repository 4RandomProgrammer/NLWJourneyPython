import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { CreateTripPage } from "./pages/create-trip";
import { TripDetailsPage } from "./pages/trip-details";
import { GuestConfirmationPage } from "./pages/guest-confirmation";

const router = createBrowserRouter([
  {
    path: "/",
    element: <CreateTripPage />,
  },
  {
    path: "/trips/:tripId",
    element: <TripDetailsPage />,
  },
  {
    path: "/participants/:participantId/confirm",
    element: <GuestConfirmationPage />,
  },
]);

export function App() {
  return <RouterProvider router={router} />;
}
