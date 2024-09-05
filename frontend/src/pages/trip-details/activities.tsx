import { CircleCheck } from "lucide-react";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { api } from "../../lib/axios";
import { format } from "date-fns";
import { ptBR } from "date-fns/locale";

interface ActivityData {
  date: string;
  activities: {
    id: string;
    title: string;
    occurs_at: string;
  }[];
}

export function Actvities() {
  const { tripId } = useParams();
  const [activities, setActivities] = useState<ActivityData[]>([]);

  useEffect(() => {
    api
      .get(`/trips/${tripId}/activities`)
      .then((response) => setActivities(response.data.activities));
  }, [tripId]);

  return (
    <div className="space-y-8">
      {activities ? (
        activities.map((category) => {
          return (
            <div key={category.date} className="space-y-2.5">
              <div className="flex gap-2 items-baseline">
                <span className="text-xl text-zinc-300 font-semibold">
                  Dia {format(category.date, "d")}
                </span>
                <span className="text-xs text-zinc-500">
                  {format(category.date, "EEEE", { locale: ptBR })}
                </span>
              </div>
              {category.activities.length > 0 ? (
                <div className="space-y-2.5">
                  {category.activities.map((activity) => {
                    return (
                      <div
                        key={activity.id}
                        className="px-4 py-2.5 bg-zinc-900 rounded-xl shadow-shape flex items-center gap-3"
                      >
                        <CircleCheck className="size-5 text-lime-300" />
                        <span className="text-zinc-100 ">{activity.title}</span>
                        <span className="text-zinc-400 text-sm ml-auto">
                          {activity.occurs_at}h
                        </span>
                      </div>
                    );
                  })}
                </div>
              ) : (
                <p className="text-zinc-500 text-sm">
                  Nenhuma atividade cadastrada nessa data.
                </p>
              )}
            </div>
          );
        })
      ) : (
        <p className="text-zinc-500 text-xl">
          Nenhuma atividade Planejada para essa viagem
        </p>
      )}
    </div>
  );
}
